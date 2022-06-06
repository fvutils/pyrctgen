'''
Created on May 13, 2022

@author: mballance
'''
from rctgen.impl.field_model_info import FieldModelInfo


class FieldClaimImpl(object):
    
    def __init__(self, name, lib_field, typeinfo):
        self._modelinfo = FieldModelInfo(self, name)
        self._modelinfo._lib_obj = lib_field
        self._modelinfo._typeinfo = typeinfo
        
    