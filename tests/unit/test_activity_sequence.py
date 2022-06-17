'''
Created on Jun 12, 2022

@author: mballance
'''
import rctgen as rg
from test_base import TestBase
from rctgen.impl.ctor import Ctor
import asyncio

class TestActivitySequence(TestBase):
    
    def test_simple_seq(self):
        
        @rg.component
        class Top(object):
            
            @rg.action
            class A(object):
                @rg.constraint
                def my_c(self):
                    pass
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
                    with rg.do[Top.B]:
                        pass
                    
                    rg.do[Top.B]
                   
                    # Could probably handle via a special-purpose __getattribute__
                    self.a()
                    
                    with self.b(1,2,3):
                        pass

        top = Top()
        asyncio.run(top.eval(Top.Entry))
        
        

        