'''
Created on May 12, 2022

@author: mballance
'''

import rctgen as rg
from test_base import TestBase

class TestPoolSmoke(TestBase):
    
    def test_smoke(self):
        
        @rg.resource
        class MyResource(object):
            pass
        
        @rg.component
        class PssTop(object):
            channels : rg.pool[MyResource] = rg.pool.size(2)
            
            @rg.exec.init_down
            def init_down(self):
                print("PssTop::init")
                self.channels.size = 20
            
        pss_top = PssTop()
            
        