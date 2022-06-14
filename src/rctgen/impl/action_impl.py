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
                if not ctor.is_type_mode():
                    s.lib_scope.setFieldData(self)
            elif s.facade_obj is self:
                s.inc_inh_depth()
            else:
                # Need to create a new scope
                if ctor.is_type_mode():
                    raise Exception("Should not hit in type mode")
                s = ctor.push_scope(
                    self,
                    ctor.ctxt().buildModelAction(
                        typeinfo.lib_obj,
                        type(self).__name__),
                    False)
                s.lib_scope.setFieldData(self)
        else:
            # Push a new scope, knowing that we're not in type mode
            if ctor.is_type_mode():
                raise Exception("Should not hit in type mode")
            s = ctor.push_scope(
                self,
                ctor.ctxt().buildModelAction(
                    typeinfo.lib_obj,
                    type(self).__name__),
                False)
            s.lib_scope.setFieldData(self)

        
        self._modelinfo = ModelInfo(self, "<>")
        self._modelinfo._lib_obj = s._lib_scope
        
        print("__init__")
        
        # Add built-in 'comp' field
        
        # Populate the fields
        # Note: cannot ask for the object representation from DataClasses
        # before this step is performed
        for i,fc in enumerate(typeinfo._field_ctor_l):
            print("Action Field: %s" % fc[0])
            ctor.push_scope(None, s.lib_scope.getField(i))
            field_facade = fc[1](fc[0])
            setattr(self, fc[0], field_facade)
            ctor.pop_scope()

        if not ctor.is_type_mode():            
            print("field_data: %s" % str(s.lib_scope.getFieldData()))
            

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
        
    @staticmethod
    def _createInst(cls, name):
        ret = cls()
        return ret
    
    @classmethod
    def addMethods(cls, T):
        ImplBase.addMethods(T)
        base_init = T.__init__
        setattr(T, "__super_init__", getattr(T, "__init__"))
        setattr(T, "__init__", lambda self, *args, **kwargs: cls.init(
            self, base_init, *args, **kwargs))
        setattr(T, "_createInst", cls._createInst)

