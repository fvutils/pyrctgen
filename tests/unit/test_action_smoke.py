'''
Created on Mar 19, 2022

@author: mballance
'''
from test_base import TestBase
from libarl import core
import asyncio

functions = []
def presolve(T):
    global functions
    print("presolve: %s" % T)
    f = exec(T)
#    print("presolve method %s" % T.__qualname__)
    functions.append(T)
    return None

class TestActionSmoke(TestBase):
    
    arl = core.Arl.inst()
    
    ctx = arl.mkContext()
    
    print("ctx=%s" % str(ctx))
    
    def test_smoke(self):
        import rctgen as rg
        
        def do_print(msg):
            print("Msg: %s" % msg)

        @rg.component            
        class MyComponent:
            pass
        
        @rg.action(MyComponent)
        class MyAction(object):
            
            @rg.exec.body
            async def body(self):
                nonlocal do_print
                do_print("Hello")

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
            
            
            pass

        root = MyComponent()
        root.eval(my_action2)
        
        a = my_action()
        a.activity()
        
        
        