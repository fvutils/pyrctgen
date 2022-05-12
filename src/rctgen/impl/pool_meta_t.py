'''
Created on May 12, 2022

@author: mballance
'''
from rctgen.impl.pool_t import PoolT
from rctgen.impl.pool_size import PoolSize

class PoolMetaT(type):
    
    def __init__(self, name, bases, dct):
        self.type_m = {}
        
    def __getitem__(self, item):
        if item in self.type_m.keys():
            return self.type_m[item]
        else:
            t = type("pool_t[%s]" % item.__qualname__, (PoolT,), {})
            t.T = item
            return t
        
    def size(self, sz):
        return PoolSize(sz)