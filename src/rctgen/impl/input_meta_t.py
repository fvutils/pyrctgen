'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.input_output_t import InputOutputT

class InputMetaT(type):

    def __init__(self, name, bases, dct):
        self.type_m = {}
        
    def __getitem__(self, item):
        if item in self.type_m.keys():
            return self.type_m[item]
        else:
            t = type("input[%s]" % item.__qualname__, (InputOutputT,), {})
            self.type_m[item] = t
            t.T = item
            t.IsInput = True
            return t    