'''
Created on Apr 4, 2022

@author: mballance
'''
import dataclasses
from rctgen.impl.ctor import Ctor
from rctgen.impl.type_info import TypeInfo
from rctgen.impl.type_kind_e import TypeKindE
from rctgen.impl.exec_group import ExecGroup
from rctgen.impl.rand_t import RandT
from rctgen.impl.scalar_t import ScalarT


class DecoratorImplBase(object):
    
    def __init__(self, kind):
        self._kind = kind
        self._supports_constraints = True
    
    def populate_execs(self, ti : TypeInfo, supported_s):
                
        return None
                
    def __call__(self, T):
        ctor = Ctor.inst()

        Tp = dataclasses.dataclass(T, init=False)

        ds_t = self._mkLibDataType(T.__qualname__, ctor.ctxt())
        ti = self._mkTypeInfo(self._kind)
        
        setattr(T, "_typeinfo", ti)
        ti.lib_obj = ds_t
        
        self._populateFields(ti, Tp)

        #************************************************************        
        #* Populate constraints from this type and base types
        #************************************************************        
        constraints = Ctor.inst().pop_constraint_decl()
        constraint_s = set()
        for c in constraints:
            constraint_s.add(c._name)
            ti._constraint_l.append(c)
            
        for b in T.__bases__:
            if hasattr(b, "_typeinfo"):
                self._populateConstraints(
                    ti, 
                    b,
                    constraint_s)
                
        #************************************************************        
        #* Populate exec blocks from this type and base types
        #************************************************************        
        execs = Ctor.inst().pop_exec_types()
        
        for e in execs:
            print("Exec: %s" % str(e.kind))
            if not self._validateExec(e.kind):
                raise Exception("Unsupported exec kind %s" % str(e.kind))
            if e.kind not in ti._exec_m.keys():
                ti._exec_m[e.kind] = ExecGroup(e.kind)
                
            ti._exec_m[e.kind].add_exec(e)
            
        for b in T.__bases__:
            if hasattr(b, "_typeinfo"):
                self._populateExecs(
                    ti, 
                    b)
        
        return Tp
    
    def _validateExec(self, kind):
        return True
    
    def _validateField(self, name, type, is_rand):
        return True
    
    def _mkTypeInfo(self, kind : TypeKindE):
        return TypeInfo(kind)
    
    def _mkLibDataType(self, name, ctxt):
        raise NotImplementedError("_mkLibDataType not implemented for %s" % str(type(self)))
    
    def _populateFields(self, ti, T):
        for f in dataclasses.fields(T):
            
            is_rand = False
            t = f.type
            if issubclass(t, RandT):
                t = t.T
                is_rand = True
                
            if issubclass(t, ScalarT):
                print("Scalar: %d" % t.W)
            elif hasattr(t, "_typeinfo"):
                print("Has TypeInfo")
                
            print("Field: %s" % str(f))
        pass
    
    def _populateExecs(self, ti, T):
        T_ti = T._typeinfo

        for kind in T_ti._exec_m.keys():

            # If the target type hasn't registered an exec of this kind,
            # but a base type has, then link that up            
            if kind not in ti._exec_m.keys():
                ti._exec_m[kind] = T_ti.exec_m[kind]
            elif ti._exec_m[kind].super is None:
                # Link the first available super-type exec to the
                # 'super' link
                ti._exec_m[kind].super = T_ti.exec_m[kind]
                
        # Now, continue working back through the inheritance hierarchy
        for b in T.__bases__:
            if hasattr(b, "_typeinfo"):
                self._populateExecs(
                    ti, 
                    b)

    def _populateConstraints(self, ti, T, name_s):
        T_ti = T._typeinfo
        
        for c in T_ti.constraint_l:
            if c.name not in name_s:
                name_s.add(c.name)
                ti.constraint_l.append(c)
                
        for b in T.__bases__:
            if hasattr(b, "_typeinfo"):
                self._populateConstraints(
                    ti, 
                    b,
                    name_s)

