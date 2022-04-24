'''
Created on Apr 24, 2022

@author: mballance
'''

class RtCtxt(object):
    
    _inst = None
    
    def __init__(self):
        self._exec_group_s = []
    
    def push_exec_group(self, g):
        self._exec_group_s.append(g)
        
    def exec_group(self):
        if len(self._exec_group_s) > 0:
            return self._exec_group_s[-1]
        else:
            return None
        
    def pop_exec_group(self):
        self._exec_group_s.pop()
    
    @classmethod
    def inst(cls):
        if cls._inst is None:
            cls._inst = RtCtxt()
        return cls._inst
    