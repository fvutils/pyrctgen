'''
Created on Mar 19, 2022

@author: mballance
'''
import inspect
from rctgen.impl.exec_type import ExecType
from rctgen.impl.exec_kind_e import ExecKindE
from rctgen.impl.ctor import Ctor

class ExecDecoratorImpl(object):
    
    def __init__(self, kind, kwargs):
        self._kind = kind
        
    def __call__(self, T):
        if self._kind in (ExecKindE.Body,):
            if not inspect.iscoroutinefunction(T):
                raise Exception("exec-block kind %s must be async" % str(self._kind))
        et = ExecType(self._kind, T)
        Ctor.inst().push_exec_type(et)
        return T