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
            
        pss_top = PssTop()
            
        