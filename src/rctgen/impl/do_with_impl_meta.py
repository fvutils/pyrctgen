'''
Created on Apr 30, 2022

@author: mballance
'''
from rctgen.impl.do_with_impl import DoWithImpl

class DoWithImplMeta(type):

    def __init__(self, name, bases, dct):
        pass
        
    def __getitem__(self, item):
        print("DoWithImplMeta: %s" % str(item._typeinfo._lib_obj))
        return DoWithImpl()
        pass    