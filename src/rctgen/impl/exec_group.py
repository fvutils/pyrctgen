'''
Created on Apr 24, 2022

@author: mballance
'''

class ExecGroup(object):
    
    def __init__(self, kind):
        self._kind = kind
        self._super = None
        self._exec_l = []
        
    @property
    def super(self):
        return self.super
    
    @super.setter
    def super(self, s):
        self._super = s
        
    @property
    def execs(self):
        return self._exec_l
    
    def add_exec(self, e):
        self._exec_l.append(e)