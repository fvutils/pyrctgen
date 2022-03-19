'''
Created on Mar 19, 2022

@author: mballance
'''
from test_base import TestBase

class TestActionSmoke(TestBase):
    
    def test_action_io(self):
        import rctgen as rg

        @rg.buffer        
        class S:
            pass
        
        @rg.action
        class my_action():
            dat_i : rg.input[S]
            dat_o : rg.output[S]
            
            @rg.exec.body
            def body(self):
                pass
            
            @rg.activity
            def activity(self):
                with rg.parallel:
                    print("")
                with rg.parallel(label="foo"):
                    print("other")
                pass
            
            pass
        
        a = my_action()
        a.activity()
        
        