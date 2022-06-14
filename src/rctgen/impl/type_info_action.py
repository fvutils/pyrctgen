'''
Created on May 8, 2022

@author: mballance
'''
from rctgen.impl.type_info import TypeInfo
from rctgen.impl.type_kind_e import TypeKindE
from rctgen.impl.ctor import Ctor
import typing

class TypeInfoAction(TypeInfo):
    
    def __init__(self, Tp):
        super().__init__(Tp, TypeKindE.Action)
        self._activity_decl_l = []
        self._component_t = None
        
    def addActivityDecl(self, a):
        self._activity_decl_l.append(a)
        
    def elab(self):
        if self._is_elab:
            return
        
        ctor = Ctor.inst()
        
        self._elabFields()

        # Build out a type model
        at = ctor.ctxt().mkDataTypeAction(self._Tp.__qualname__)
        ctor.push_scope(None, at, True)
        obj = self._Tp()
        
        # Elaboate constraints
        ctor.push_expr_mode()
        for c in self._constraint_l:
            c.func(obj)
            
        for a in self._activity_decl_l:
            a.func(obj)

        ctor.pop_expr_mode()        
        ctor.pop_scope()
                
        self._is_elab = True
        
    