'''
Created on Mar 19, 2022

@author: mballance
'''
from test_base import TestBase
from libarl import core
import asyncio
import rctgen as rg
from rctgen.impl.ctor import Ctor
import dataclasses

functions = []
def presolve(T):
    global functions
    print("presolve: %s" % T)
    f = exec(T)
#    print("presolve method %s" % T.__qualname__)
    functions.append(T)
    return None

class TestActionSmoke(TestBase):
    
    def test_smoke(self):
        
        def do_print(msg):
            print("Msg: %s" % msg)

        @rg.component
        class MySubComponent:
            v : rg.int8_t = 3
            
            @rg.exec.init_down
            def init_down(self):
                print("MySubComponent::init_down: %d" % self.v)
                self.v = 7
                print("MySubComponent::init_down: %d" % self.v)
            pass
        
        @rg.component            
        class MyComponent:
            val : rg.int8_t = 2
            sc : MySubComponent
            
            @rg.exec.init_down
            def init_down(self):
                print("init_down")
                
            pass
        
        @rg.action(MyComponent)
        class MyBaseAction(object):
            
            @rg.exec.body
            async def body(self):
                nonlocal do_print
                do_print("Hello Base")
        
        @rg.action(MyComponent)
        class MyAction(object):
            
            @rg.exec.body
            async def body(self):
                nonlocal do_print
                do_print("Hello")
                await self.super()

        root_c = MyComponent()
        asyncio.run(root_c.eval(MyAction))                
    
    def test_action_io(self):
        import rctgen as rg
        
        def do_print(msg):
            print("Msg: %s" % msg)

        @rg.buffer
        class S:
            pass

        @rg.component
        class MyComponent:
            pass
        
        @rg.action(MyComponent)
        class my_action():
            dat_i : rg.input[S]
            dat_o : rg.output[S]
            
            @rg.exec.body
            def body(self):
                nonlocal do_print
                do_print("Hello")
            
            @rg.activity
            def activity(self):
                with rg.parallel:
                    print("")
                with rg.parallel(label="foo"):
                    print("other")
                pass
            
        @rg.action(component=MyComponent)
        class my_action2():
            dat_i : rg.input[S]
            dat_o : rg.output[S]
            
            @rg.exec.body
            def body(self):
                print("Hello from exec body")
                pass
            
            @rg.exec.body
            def _body(self):
                print("Hello")
                pass
            
            @rg.activity
            def activity(self):
                with rg.parallel:
                    print("")
                with rg.parallel(label="foo"):
                    print("other")

        root = MyComponent()
        root.eval(my_action2)
        
        a = my_action()
        a.activity()
        
    def test_activity_basics(self):

#         def cg(T):
#             print("cg")
#             T.A : int = 1
#             Tp = dataclasses.dataclass(T, init=False)
#
#             for f in dataclasses.fields(Tp):
#                 print("Field: %s" % f.name)
#                 if f.default is not dataclasses.MISSING:
# #                    f.default()
#                     pass
#             return Tp
#
#         def init():
#             print("init")
#             return None
#
#         def wrap(o):
#             pass
#
#         def coverpoint(t):
#             print("Target: %s" % str(t))
#             return 0
#
#         def cross(*args):
#             pass
#
#         @cg
#         class foo:
#             A : int = lambda: coverpoint(0).body(
#                 iff(2),
#                 bins={
#                     }
#                 ).iff(2<10).bins({
#                     a : bin(20)
#                     })
#             F : int = lambda: coverpoint(A)
#             G : int = lambda: coverpoint(F)
#             FxG : cross = lambda: cross(A,F).iff(F+G < 10).options(
#                                    options())
        
        @rg.component
        class MyComponent(object):
        
            @rg.action
            class SayHello(object):
            
                val : rg.rand_uint16_t
            
                @rg.exec.body
                async def body(self):
                    print("Hello %d" % self.val)
        
            @rg.action
            class MyAction(object):
            
                @rg.activity
                def activity(self):
                    rg.do[MyComponent.SayHello]
                    with rg.do_with[MyComponent.SayHello] as it:
                        pass
        
#        ctor = Ctor.inst()
#        ctor.elab()
        
        root_comp = MyComponent()
        asyncio.run(root_comp.eval(MyComponent.MyAction))                
            
#        a = MyAction()
#        a.activity()
            
        