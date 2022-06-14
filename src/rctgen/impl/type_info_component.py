'''
Created on Jun 2, 2022

@author: mballance
'''
from rctgen.impl.type_info import TypeInfo
from rctgen.impl.type_kind_e import TypeKindE
import typing
import dataclasses

class TypeInfoComponent(TypeInfo):
    
    def __init__(self, Tp):
        super().__init__(Tp, TypeKindE.Component)
        self._action_t = []
        
    def elab(self):
        # First, fixup indirect type references
        name_m = {
            self._Tp.__name__ : self._Tp
        }
        for a in self._action_t:
            if a.__name__ not in name_m.keys():
                name_m[a.__name__] = a

        for a in self._action_t:
            hints = typing.get_type_hints(a, name_m)
            
            for f in dataclasses.fields(a):
                if f.name in hints.keys():
                    object.__setattr__(f, "type", hints[f.name])

        # Now, go and elaborate the action type
        for a in self._action_t:
            a._typeinfo.elab()
        self._is_elab = True
