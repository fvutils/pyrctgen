'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.action_decorator_impl import ActionDecoratorImpl
from rctgen.impl.exec_decorator_impl import ExecDecoratorImpl
from rctgen.impl.exec_kind_e import ExecKindE
from rctgen.impl.struct_decorator_impl import StructDecoratorImpl
from rctgen.impl.struct_kind_e import StructKindE
from rctgen.impl.component_decorator_impl import ComponentDecoratorImpl
from rctgen.impl.activity_decorator_impl import ActivityDecoratorImpl
from rctgen.impl.type_kind_e import TypeKindE

def action(*args, **kwargs): 
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        if hasattr(args[0], "_typeinfo") and args[0]._typeinfo.kind == TypeKindE.Component:
            # Argument form with the parameter being the context class
            return ActionDecoratorImpl(args, kwargs)
        else:
            # No-argument form
            return ActionDecoratorImpl([], {})(args[0])
    else:
        # Argument form
        return ActionDecoratorImpl(args, kwargs)
    
def activity(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # No-argument form
        return ActivityDecoratorImpl({})(args[0])
    else:
        return ActivityDecoratorImpl(kwargs)
    
def component(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # No-argument form
        return ComponentDecoratorImpl({})(args[0])
    else:
        return ComponentDecoratorImpl(kwargs)
    
def buffer(*args, **kwargs): 
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # No-argument form
        return StructDecoratorImpl(StructKindE.Buffer, {})(args[0])
    else:
        return ActionDecoratorImpl(StructKindE.Buffer, kwargs)
    
def resource(*args, **kwargs): 
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # No-argument form
        return StructDecoratorImpl(StructKindE.Resource, {})(args[0])
    else:
        return ActionDecoratorImpl(StructKindE.Resource, kwargs)
    
def state(*args, **kwargs): 
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # No-argument form
        return StructDecoratorImpl(StructKindE.State, {})(args[0])
    else:
        return ActionDecoratorImpl(StructKindE.State, kwargs)
    
def stream(*args, **kwargs): 
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # No-argument form
        return StructDecoratorImpl(StructKindE.Stream, {})(args[0])
    else:
        return ActionDecoratorImpl(StructKindE.Stream, kwargs)
    
def struct(*args, **kwargs): 
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # No-argument form
        return StructDecoratorImpl(StructKindE.Struct, {})(args[0])
    else:
        return ActionDecoratorImpl(StructKindE.Struct, kwargs)

class exec(object):
    @staticmethod
    def body(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            # No-argument form
            return ExecDecoratorImpl(ExecKindE.Body, {})(args[0])
        else:
            return ExecDecoratorImpl(ExecKindE.Body, kwargs)
        
    @staticmethod
    def pre_solve(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            # No-argument form
            return ExecDecoratorImpl(ExecKindE.PreSolve, {})(args[0])
        else:
            return ExecDecoratorImpl(ExecKindE.PreSolve, kwargs)
        
    @staticmethod
    def post_solve(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            # No-argument form
            return ExecDecoratorImpl(ExecKindE.PostSolve, {})(args[0])
        else:
            return ExecDecoratorImpl(ExecKindE.PostSolve, kwargs)
    
