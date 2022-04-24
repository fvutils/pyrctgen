'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.decorator_impl_base import DecoratorImplBase
from rctgen.impl.type_kind_e import TypeKindE
from rctgen.impl.exec_kind_e import ExecKindE

class StructDecoratorImpl(DecoratorImplBase):
    
    def __init__(self, kind, kwargs):
        super().__init__(TypeKindE.Struct)
        self._kind = kind
        
    def __call__(self, T):
        Tp = super().__call__(T)
        
        # TODO: Add methods
        
        return Tp
    
    def _validateExec(self, kind):
        return kind in [ExecKindE.PreSolve, ExecKindE.PostSolve]
    
    def _mkLibDataType(self, name, ctxt):
        ds_t = ctxt.findDataTypeStruct(name)
        
        if ds_t is None:
            ds_t = ctxt.mkDataTypeStruct(name)
            ctxt.addDataTypeStruct(ds_t)

        return ds_t
