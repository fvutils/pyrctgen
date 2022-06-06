'''
Created on Apr 4, 2022

@author: mballance
'''
from typing import Dict, List, Tuple
from rctgen.impl.exec_kind_e import ExecKindE
from rctgen.impl.exec_group import ExecGroup
from rctgen.impl.constraint_impl import ConstraintImpl

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
