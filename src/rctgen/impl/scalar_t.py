'''
Created on Apr 26, 2022

@author: mballance
'''

from .field_scalar_impl import FieldScalarImpl
from .ctor import Ctor
from rctgen.impl.ctor_scope import CtorScope

class ScalarT(FieldScalarImpl):
    W = 0
    S = False
    
    def __init__(self, name="", iv=0):
        ctor = Ctor.inst()
        # TODO: need to check construction mode, etc?
        
        # Create a model field based on the relevant signedness/size
        lib_type = ctor.ctxt().findDataTypeInt(type(self).S, type(self).W)
        if lib_type is None:
            lib_type = ctor.ctxt().mkDataTypeInt(type(self).S, type(self).W)
            ctor.ctxt().addDataTypeInt(lib_type)
            
        
        lib_field = ctor.ctxt().mkModelFieldRoot(
            lib_type,
            name)
        
        if type(self).W <= 64:
            if type(self).S:
                lib_field.val().set_val_i(iv)
            else:
                lib_field.val().set_val_u(iv)
        else:
            raise Exception("Field >64 not yet supported")
        
        super().__init__(name, lib_field, type(self).S)

    @classmethod
    def createField(cls, name):
        print("ScalarT::create %d %d" % (cls.W, cls.S))
        ctor = Ctor.inst()
        s : CtorScope = ctor.scope()
        ret = FieldScalarImpl(
            name, 
            s.lib_scope,
            cls.S)
        
        return ret
    