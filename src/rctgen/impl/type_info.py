'''
Created on Apr 4, 2022

@author: mballance
'''
import dataclasses
from libvsc import core as vsc
from typing import Dict, List, Tuple
from rctgen.impl.exec_kind_e import ExecKindE
from rctgen.impl.exec_group import ExecGroup
from rctgen.impl.constraint_impl import ConstraintImpl
from rctgen.impl.rand_t import RandT
from rctgen.impl.ctor import Ctor
from rctgen.impl.scalar_t import ScalarT
from rctgen.impl.pool_t import PoolT
from rctgen.impl.lock_share_t import LockShareT

class TypeInfo(object):
    
    def __init__(self, Tp, kind):
        
        self._Tp = Tp
        
        self._is_elab = False
        
        self._kind = kind
        
        self._lib_obj = None
        
        # Only meaningful for actions
        self._ctxt_t = None

        # Dict of exec kind to list of exec blocks
        self._exec_m : Dict[ExecKindE,ExecGroup] = {}
        
        # List of constraints
        self._constraint_l : List[ConstraintImpl] = []
        
        # List of field-name, field-constructor
        self._field_ctor_l : Tuple[str,object] = []
        
    @property
    def kind(self):
        return self._kind
    
    @kind.setter
    def kind(self, _kind):
        self._kind = _kind
        
    @property
    def lib_obj(self):
        return self._lib_obj
    
    @lib_obj.setter
    def lib_obj(self, o):
        self._lib_obj = o
        
    @property
    def ctxt_t(self):
        return self._ctxt_t
    
    @ctxt_t.setter
    def ctxt_t(self, _ctxt_t):
        self._ctxt_t = _ctxt_t
        
    @property
    def is_elab(self):
        return self._is_elab
    
    def elab(self):
        raise NotImplementedError("elab not implemented for type %s" % str(type(self)))
        self._is_elab = True
        
    def _elabFields(self):
        for f in dataclasses.fields(self._Tp):

            attr = vsc.ModelFieldFlag.NoFlags
            is_rand = False
            iv=0

            if type(f.type) == str:
#                raise Exception("Type %s is forward declared" % t)
                raise Exception("Field %s has an unresolved type %s" % (f.name, f.type))
            
            t = f.type

            if issubclass(t, RandT):
                t = t.T
                attr |= vsc.ModelFieldFlag.DeclRand
                is_rand = True

            ctor = Ctor.inst()

            print("f: %s" % str(f))
            
            # The signature of a creation function is:
            # - name
            # - is_rand
            # - idx
            if issubclass(t, ScalarT):
                self._elabFieldScalar(f, attr, t)
            elif issubclass(t, PoolT):
                self._elabFieldPool(f, attr, t)
            elif issubclass(t, LockShareT):
                print("LockShare!")
                self._elabFieldLockShare(f, attr, t)
            elif hasattr(t, "_typeinfo") and isinstance(t._typeinfo, TypeInfo):
                # This is a field of user-defined type
                print("Has TypeInfo")
                field_t = ctor.ctxt().mkTypeFieldPhy(
                    f.name, 
                    t._typeinfo.lib_obj,
                    False,
                    attr,
                    None)
                self.lib_obj.addField(field_t)
                self._field_ctor_l.append((f.name, lambda name, t=t: t._createInst(t, name)))
                
            print("Field: %s" % str(f))
            
    def _elabFieldLockShare(self, f, attr, t):
        ctor = Ctor.inst()
        
        if hasattr(t.T, "_typeinfo"):
            print("Kind: %s" % str(t.T._typeinfo._kind))
            claim_t = t.T._typeinfo.lib_obj
        else:
            raise Exception("Type %s is not a PyRctGen type" % t.T.__qualname__)
        
        if f.default is not dataclasses.MISSING:
            print("default: %s" % str(f.default))
            raise Exception("Lock/Share fields cannot be assigned a value")
        
        field_t = ctor.ctxt().mkTypeFieldClaim(
            f.name,
            claim_t,
            t.IsLock)

        self.lib_obj.addField(field_t)
        self._field_ctor_l.append((f.name, t.createField))        

    def _processFieldPool(self, ti, f, attr, t):
        ctor = Ctor.inst()
        decl_size = -1
        
        pool_t = None
        
        if hasattr(t.T, "_typeinfo"):
            print("Kind: %s" % str(t.T._typeinfo._kind))
            pool_t = t.T._typeinfo.lib_obj
        else:
            raise Exception("Type %s is not a PyRctGen type" % t.T.__qualname__)
        
        if f.default is not dataclasses.MISSING:
            if t.T._typeinfo._kind != StructKindE.Resource:
                raise Exception("Only resource pools may be given a size. Pool %s is of kind %s" % (
                    f.name, t.T._typeinfo._kind))
            decl_size = int(f.default)
        
        field_t = ctor.ctxt().mkTypeFieldPool(
            f.name,
            pool_t,
            attr,
            decl_size)

        ti.lib_obj.addField(field_t)
        ti._field_ctor_l.append((f.name, t.createField))
        
    def _elabFieldScalar(self, f, attr, t):
        ctor = Ctor.inst()
        lt = ctor.ctxt().findDataTypeInt(t.S, t.W)
        if lt is None:
            lt = ctor.ctxt().mkDataTypeInt(t.S, t.W)
            ctor.ctxt().addDataTypeInt(lt)

        iv_m = None
        
        if f.default is not dataclasses.MISSING:
            iv_m = ctor.ctxt().mkModelVal()
            iv_m.setBits(t.W)
            if t.S:
                iv_m.set_val_i(int(f.default))
            else:
                iv_m.set_val_u(int(f.default))
            
        field_t = ctor.ctxt().mkTypeFieldPhy(
            f.name, 
            lt, 
            attr,
            iv_m)
        self.lib_obj.addField(field_t)
        self._field_ctor_l.append((f.name, t.createField))        
