'''
Created on Apr 4, 2022

@author: mballance
'''
from typing import Dict, List
from rctgen.impl.exec_kind_e import ExecKindE

class TypeInfo(object):
    
    def __init__(self, kind):
        self._kind = kind
        
        # Only meaningful for actions
        self._ctxt_t = None

        # Dict of exec kind to list of exec blocks
        self._exec_m : Dict[ExecKindE,List] = {}
        
    @property
    def kind(self):
        return self._kind
    
    @kind.setter
    def kind(self, _kind):
        self._kind = _kind
        
    @property
    def ctxt_t(self):
        return self._ctxt_t
    
    @ctxt_t.setter
    def ctxt_t(self, _ctxt_t):
        self._ctxt_t = _ctxt_t
