'''
Created on May 12, 2022

@author: mballance
'''
from rctgen.impl.field_model_info import FieldModelInfo

class FieldPoolImpl(object):
    
    def __init__(self, name, lib_field):
        self._modelinfo = FieldModelInfo(self, name)
        
        self._modelinfo._lib_obj = lib_field

    @property
    def size(self):
        return 0
    
    @size.setter
    def size(self, v):
        print("Set size: %d" % v)
        
    