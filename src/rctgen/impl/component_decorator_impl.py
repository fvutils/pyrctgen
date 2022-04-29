'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.type_info import TypeInfo
from rctgen.impl.type_kind_e import TypeKindE
from rctgen.impl.decorator_impl_base import DecoratorImplBase
from rctgen.impl.component_impl import ComponentImpl
from rctgen.impl.exec_kind_e import ExecKindE


class ComponentDecoratorImpl(DecoratorImplBase):

    def __init__(self, kwargs):
        super().__init__(TypeKindE.Component)
        pass
    
    def __call__(self, T):
        Tp = super().__call__(T)
        
        ComponentImpl.addMethods(T)
        
        return Tp
    
    def _validateExec(self, kind):
        return kind in (ExecKindE.InitDown, ExecKindE.InitUp)

    def _mkLibDataType(self, T, name, ctxt):
        ds_t = ctxt.findDataTypeComponent(name)
        
        if ds_t is None:
            ds_t = ctxt.mkDataTypeComponent(name)
            ctxt.addDataTypeComponent(ds_t)
        
        return ds_t
        