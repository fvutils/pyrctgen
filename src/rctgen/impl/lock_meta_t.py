'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.lock_share_t import LockShareT

class LockMetaT(type):
    
    def __init__(self, name, bases, dct):
        self.type_m = {}
        
    def __getitem__(self, item):
        if item in self.type_m.keys():
            return self.type_m[item]
        else:
            t = type("lock[%s]" % item.__qualname__, (LockShareT,), {})
            self.type_m[item] = t
            t.T = item
            t.IsLock = True
            return t        