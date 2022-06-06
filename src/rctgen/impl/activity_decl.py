'''
Created on May 8, 2022

@author: mballance
'''

class ActivityDecl(object):
    
    def __init__(self, func):
        self._func = func
        
    @property
    def func(self):
        return self._func
    