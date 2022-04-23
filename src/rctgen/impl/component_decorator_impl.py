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
        pass
    
    def __call__(self, T):
        setattr(T, "_typeinfo", TypeInfo(TypeKindE.Component))
        ComponentImpl.add_methods(T)
        
        self.populate_execs(
            T._typeinfo,
            (ExecKindE.InitDown, ExecKindE.InitUp))
        return T
