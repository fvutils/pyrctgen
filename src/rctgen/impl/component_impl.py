'''
Created on Apr 4, 2022

@author: mballance
'''
from libarl import core
from rctgen.impl.ctor import Ctor
from rctgen.impl.model_info import ModelInfo
from rctgen.impl.type_info import TypeInfo
from rctgen.impl.exec_kind_e import ExecKindE
from rctgen.impl.exec_group import ExecGroup
from rctgen.impl.rt_ctxt import RtCtxt
from rctgen.impl.impl_base import ImplBase

class ComponentImpl(ImplBase):
    """Methods added to Component-decorated classes"""
    
    @staticmethod
    async def eval(self, action_t):
        print("ComponentImpl.eval")
        ctor = Ctor.inst()
        ev = ctor.ctxt().mkModelEvaluator()
        it = ev.eval(
            self._modelinfo._lib_obj,
            action_t._typeinfo._lib_obj)

        print("Iterating...")        
        while it.next():
            if it.type() == core.ModelEvalNodeT.Action:
                action_field = it.action()
                action = action_field.getFieldData()
                await action._evalExecTarget(ExecKindE.Body)
            
                print("Action: %s" % str(action))
            elif it.type() == core.ModelEvalNodeT.Parallel:
                # Create a coroutine for each branch
                # Wait for coroutines to complete
                print("TODO: evaluate parallel")
                pass
            elif it.type() == core.ModelEvalNodeT.Sequence:
                # Iterate through each item and dispatch
                print("TODO: evaluate sequence")
                pass
            print("type: %s" % str(it.type()))
        
    @staticmethod
    def init(self, base, *args, **kwargs):
        ctor = Ctor.inst()

        # Elaborate just in case we haven't already        
        ctor.elab()
        
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
                    ctor.ctxt().buildModelComponent(
                        typeinfo.lib_obj,
                        type(self).__name__),
                    False)
                pass
            pass
        else:
            # Push a new scope, knowing that we're not in type mode
            s = ctor.push_scope(
                self,
                ctor.ctxt().buildModelComponent(
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
        
        if s.dec_inh_depth() == 0:
            if not ctor.is_type_mode():
                # Run the init sequence
                self._runInitSeq()
        
        pass
        

    @staticmethod        
    def _runInitSeq(self):
        typeinfo : TypeInfo = type(self)._typeinfo
        ctxt = RtCtxt.inst()
        
        if ExecKindE.InitDown in typeinfo._exec_m.keys():
            exec_g : ExecGroup = typeinfo._exec_m[ExecKindE.InitDown]

            ctxt.push_exec_group(exec_g)
            for e in exec_g.execs:
                e.func(self)
            ctxt.pop_exec_group()
                
        # TODO: Recurse for any component-type fields
        
        if ExecKindE.InitUp in typeinfo._exec_m.keys():
            exec_g : ExecGroup = typeinfo._exec_m[ExecKindE.InitUp]
            
            ctxt.push_exec_group(exec_g)
            for e in exec_g.execs:
                e.func(self)
            ctxt.pop_exec_group()
            
        pass
    
    @staticmethod
    def _createInst(cls, name):
        ret = cls()
        return ret
    
    @classmethod
    def addMethods(cls, T):
        ImplBase.addMethods(T)
        base_init = T.__init__
        setattr(T, "__init__", lambda self, *args, **kwargs: cls.init(
            self, base_init, *args, **kwargs))
        setattr(T, "_runInitSeq", cls._runInitSeq)
        setattr(T, "_createInst", cls._createInst)
        setattr(T, "eval", cls.eval)
        