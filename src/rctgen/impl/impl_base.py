'''
Created on Apr 4, 2022

@author: mballance
'''
from rctgen.impl.ctor import Ctor

class ImplBase(object):
    
    @staticmethod
    def setattr(self, name, v):
        try:
            fo = object.__getattribute__(self, name)
        except:
            object.__setattr__(self, name, v)
        else:
            object.__setattr__(self, name, v)
            
    @staticmethod
    def getattribute(self, name):
        ctor = Ctor.inst()
        ret = object.__getattribute__(self, name)
        
        print("ImplBase.getattr")

        if not ctor.expr_mode():
            # TODO: Check whether this is a 'special' field
            if hasattr(ret, "get_val"):
                ret = ret.get_val()
        
        return ret

    @staticmethod
    def addMethods(T):
        setattr(T, "__setattr__", ImplBase.setattr)
        setattr(T, "__getattribute__", ImplBase.getattribute)
    pass
