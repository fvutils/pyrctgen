'''
Created on May 12, 2022

@author: mballance
'''

import rctgen as rg
from test_base import TestBase
import asyncio

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
                
        @rg.action
        class Entry(object):
            rsrc : rg.lock[MyResource]
            
            @rg.exec.body
            async def body(self):
                print("Hello from body")
            pass
                
        pss_top = PssTop()
        asyncio.get_event_loop().run_until_complete(pss_top.eval(Entry))
        
        print("size: %d" % pss_top.channels.size)
        
            
        