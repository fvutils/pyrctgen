'''
Created on May 8, 2022

@author: mballance
'''
from rctgen.impl.type_info import TypeInfo
from rctgen.impl.type_kind_e import TypeKindE

class TypeInfoAction(TypeInfo):
    
    def __init__(self):
        super().__init__(TypeKindE.Action)
        self._activity_decl = []
        
    def addActivityDecl(self, a):
        self._activity_decl.append(a)
        
    