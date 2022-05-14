'''
Created on May 12, 2022

@author: mballance
'''
from rctgen.impl.field_model_info import FieldModelInfo
from rctgen.impl.ctor import Ctor
from rctgen.impl.type_kind_e import TypeKindE
from rctgen.impl.struct_kind_e import StructKindE

class FieldPoolImpl(object):
    
    def __init__(self, name, lib_field, typeinfo):
        self._modelinfo = FieldModelInfo(self, name)
        
        self._modelinfo._lib_obj = lib_field
        self._modelinfo._typeinfo = typeinfo

    @property
    def size(self):
        if self._modelinfo._typeinfo._kind != StructKindE.Resource:
            raise Exception("Size is only valid on resource pools. Pool %s is of kind %s" % (
                self.name, self._modelinfo._typeinfo._kind))
        else:
            return self._modelinfo._lib_obj.getField(0).val().val_i()
    
    @size.setter
    def size(self, v):
        ctor = Ctor.inst()
        
        if ctor.is_type_mode():
            raise Exception("Attempting to set size in type mode")
        else:
            if self._modelinfo._typeinfo._kind != StructKindE.Resource:
                raise Exception("Size can only be specified on resource pools. Pool %s is of kind %s" % (
                    self.name, self._modelinfo._typeinfo._kind))
            print("Set value to %d" % v)
            self._modelinfo._lib_obj.getField(0).val().set_val_i(v)
