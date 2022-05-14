'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.type_info import TypeInfo
from rctgen.impl.type_kind_e import TypeKindE
from rctgen.impl.decorator_impl_base import DecoratorImplBase
from rctgen.impl.action_impl import ActionImpl
from rctgen.impl.exec_kind_e import ExecKindE
from rctgen.impl.ctor import Ctor
from rctgen.impl.type_info_action import TypeInfoAction

class ActionDecoratorImpl(DecoratorImplBase):
    
    def __init__(self, args, kwargs):
        super().__init__(TypeKindE.Action)
        self._args = args
        self._kwargs = kwargs
        pass
    
    def __call__(self, T):
        ctor = Ctor.inst()
        
        ActionImpl.addMethods(T)

        component_t = None        
        if len(self._args) != 0:
            if not hasattr(self._args[0], "_typeinfo"):
                raise Exception("Type %s is not a RctGen type" % str(self._args[0]))
            if self._args[0]._typeinfo.kind != TypeKindE.Component:
                raise Exception("Type %s is of kind %s, not Component" % (
                    self._args[0].__qualname__, str(self._args[0]._typeinfo.kind)))
            component_t = self._args[0]
        elif "component" in self._kwargs.keys():
            ctxt_t = self._kwargs["component"]
            if not hasattr(ctxt_t, "_typeinfo"):
                raise Exception("Type %s is not a RctGen type" % str(ctxt_t))
            if ctxt_t._typeinfo.kind != TypeKindE.Component:
                raise Exception("Type %s is of kind %s, not Component" % (
                    ctxt_t.__qualname__, str(ctxt_t._typeinfo.kind)))
            component_t = ctxt_t
        else:
            print("Abstract action")
            
        Tp = super().__call__(T)
            
        self.populate_execs(
            Tp._typeinfo,
            (ExecKindE.PreSolve, ExecKindE.PostSolve, ExecKindE.Body))
        
        for a in ctor.pop_activity_decl():
            Tp._typeinfo.addActivityDecl(a)
        
#        self.populate_activities(Tp._typeinfo)
        
        # Build out the type model associated with this type

#        ctor.push_action_decl(Tp)
        Ctor.inst().add_action_typeinfo(Tp, Tp._typeinfo)
        
        return Tp
    
    def _mkTypeInfo(self, kind : TypeKindE):
        return TypeInfoAction()
   
    def _mkLibDataType(self, T, name, ctxt):
        ds_t = ctxt.findDataTypeAction(name)
        if ds_t is None:
            ds_t = ctxt.mkDataTypeAction(name)
            ds_t.setCreateHook(lambda obj: ActionImpl._createHook(T, obj))
            ctxt.addDataTypeAction(ds_t)
        return ds_t
    