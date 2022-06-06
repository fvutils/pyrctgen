'''
Created on Jun 2, 2022

@author: mballance
'''
from rctgen.impl.type_info import TypeInfo
from rctgen.impl.type_kind_e import TypeKindE

class TypeInfoComponent(TypeInfo):
    
    def __init__(self, Tp):
        super().__init__(Tp, TypeKindE.Component)
        self._action_t = []
        
    def elab(self):
        for a in self._action_t:
            a._typeinfo.elab()
        self._is_elab = True
