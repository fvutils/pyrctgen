'''
Created on Apr 26, 2022

@author: mballance
'''

from .rand_t import RandT

class RandTMeta(type):
    
    def __init__(self, name, bases, dct):
        self.type_m = {}
        
    def __getitem__(self, item):
        if item in self.type_m.keys():
            return self.type_m[item]
        else:
            t = type('rand_t[%s]' % str(item), (RandT,), {})
            t.T = item
            return t
