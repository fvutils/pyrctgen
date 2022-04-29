'''
Created on Apr 4, 2022

@author: mballance
'''
from rctgen.impl.impl_base import ImplBase
from rctgen.impl.ctor import Ctor
from rctgen.impl.model_info import ModelInfo

class ActionImpl(ImplBase):
    
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
                s = ctor.push_scope(
                    self,
                    ctor.ctxt().buildModelAction(
                        typeinfo.lib_obj,
                        type(self).__name__),
                    False)
                pass
            pass
        else:
            # Push a new scope, knowing that we're not in type mode
            s = ctor.push_scope(
                self,
                ctor.ctxt().buildModelAction(
                    typeinfo.lib_obj,
                    type(self).__name__),
                False)
        
        self._modelinfo = ModelInfo(self, "<>")
        self._modelinfo._lib_obj = s._lib_scope
        
        print("__init__")
        
        # Populate the fields
        for i,fc in enumerate(typeinfo._field_ctor_l):
            print("Field: %s" % fc[0])
            ctor.push_scope(None, s.lib_scope.getField(i), False)
            field_facade = fc[1](fc[0])
            setattr(self, fc[0], field_facade)
            ctor.pop_scope()
            

        # Invoke the user-visible constructor        
        base(self, *args, *kwargs)
        
        pass
    
    @staticmethod
    def _createHook(cls, hndl):
        print("createHook")
        ctor = Ctor.inst()
        ctor.push_scope(None, hndl, False)
        inst = cls()
        ctor.pop_scope()
    
    
    @classmethod
    def addMethods(cls, T):
        ImplBase.addMethods(T)
        base_init = T.__init__
        setattr(T, "__super_init__", getattr(T, "__init__"))
        setattr(T, "__init__", lambda self, *args, **kwargs: cls.init(
            self, base_init, *args, **kwargs))
        pass