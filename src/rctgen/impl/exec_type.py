'''
Created on Apr 4, 2022

@author: mballance
'''

class ExecType(object):
    
    def __init__(self, kind, f):
        self._kind = kind
        self._f = f
        
    @property
    def kind(self):
        return self._kind
    
    @kind.setter
    def kind(self, k):
        self._kind = k

    @property
    def func(self):
        return self._f
