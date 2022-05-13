'''
Created on May 12, 2022

@author: mballance
'''

class PoolSize(object):
    
    def __init__(self, sz):
        self._sz = sz
        
    def __int__(self):
        return self._sz