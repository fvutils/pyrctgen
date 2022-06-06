'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.type_info import TypeInfo
from rctgen.impl.type_kind_e import TypeKindE
from rctgen.impl.decorator_impl_base import DecoratorImplBase
from rctgen.impl.component_impl import ComponentImpl
from rctgen.impl.exec_kind_e import ExecKindE
from rctgen.impl.ctor import Ctor
from rctgen.impl.type_info_component import TypeInfoComponent


class ComponentDecoratorImpl(DecoratorImplBase):

    def __init__(self, kwargs):
        super().__init__(TypeKindE.Component)
        pass
    
    def __call__(self, T):
        ctor = Ctor.inst()
        Tp = super().__call__(T)
        
        ComponentImpl.addMethods(T)
        
        for a in ctor.pop_action_decl():
            print("Have Action")
            
            a._typeinfo._component_t = Tp
            a._typeinfo._lib_obj.setComponentType(Tp._typeinfo._lib_obj)
            
            Tp._typeinfo._action_t.append(a)
            
        ctor.add_component(T)
        
        return Tp
    
    def _validateExec(self, kind):
        return kind in (ExecKindE.InitDown, ExecKindE.InitUp)
    
    def _mkTypeInfo(self, Tp, kind:TypeKindE):
        return TypeInfoComponent(Tp)

    def _mkLibDataType(self, T, name, ctxt):
        ds_t = ctxt.findDataTypeComponent(name)
        
        if ds_t is None:
            ds_t = ctxt.mkDataTypeComponent(name)
            ctxt.addDataTypeComponent(ds_t)
        
        return ds_t
        