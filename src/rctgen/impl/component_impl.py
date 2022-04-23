'''
Created on Apr 4, 2022

@author: mballance
'''
from rctgen.impl.ctor import Ctor
from rctgen.impl.model_info import ModelInfo

class ComponentImpl(object):
    """Methods added to Component-decorated classes"""
    
    @staticmethod
    async def eval(self, action_t):
        print("ComponentImpl.eval")
        
    @staticmethod
    def init(self, base, *args, **kwargs):
        ctor = Ctor.inst()
        typeinfo = type(self)._typeinfo
        
        s = ctor.scope()
        
        if s is not None:
            if s.facade_obj is None:
                # The field-based caller has created a frame for us
                s.facade_obj = self
            elif s.facade_obj is self:
                s.inc_inh_depth()
            else:
                # Need to create a new scope
                if s._type_mode:
                    raise Exception("Should hit in type mode")
                pass
            pass
        else:
            # Push a new scope, knowing that we're not in type mode
            model = None # TODO: build from template
            s = ctor.push_scope(self, model, False)
        
        self._modelinfo = ModelInfo(self, "<>")
        self._modelinfo._lib_obj = s._lib_scope
        
        print("__init__")
        
        base(self, *args, *kwargs)
        
        if s.dec_inh_depth() == 0:
            if not ctor.is_type_mode():
                # Run the init sequence
                print("TODO: run init sequence")
        
        pass
        
    @classmethod
    def add_methods(cls, T):
        base_init = T.__init__
        setattr(T, "__init__", lambda self, *args, **kwargs: cls.init(
            self, base_init, *args, **kwargs))
        setattr(T, "eval", cls.eval)
        