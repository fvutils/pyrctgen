'''
Created on Apr 4, 2022

@author: mballance
'''
from rctgen.impl.impl_base import ImplBase

class ActionImpl(ImplBase):
    
    @staticmethod
    def init(self):
        pass
    
    @classmethod
    def add_methods(cls, T):
        setattr(T, "__super_init__", getattr(T, "__init__"))
        setattr(T, "__init__", cls.init)
        pass