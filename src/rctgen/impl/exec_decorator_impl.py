'''
Created on Mar 19, 2022

@author: mballance
'''

class ExecDecoratorImpl(object):
    
    def __init__(self, kind, kwargs):
        self._kind = kind
        
    def __call__(self, T):
        return T