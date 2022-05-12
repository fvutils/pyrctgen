'''
Created on Apr 30, 2022

@author: mballance
'''
from rctgen.impl.ctor import Ctor

class DoImplMeta(type):

    def __init__(self, name, bases, dct):
        pass
        
    def __getitem__(self, item):
        ctor = Ctor.inst()
        print("DoImplMeta: %s" % str(item._typeinfo._lib_obj))
        pass
    