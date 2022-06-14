'''
Created on Jun 12, 2022

@author: mballance
'''
import rctgen as rg
from test_base import TestBase
from rctgen.impl.ctor import Ctor

class TestActivitySequence(TestBase):
    
    def test_simple_seq(self):
        
        @rg.component
        class Top(object):
            
            @rg.action
            class A(object):
                pass
            
            @rg.action
            class B(object):
                pass
            
            @rg.action
            class Entry(object):
                a : 'A'
                b : 'B'
                
                @rg.activity
                def activity(self):
                    rg.do[Top.A]
                    rg.do[Top.B]
                    
        Ctor.inst().elab()
        
        

        