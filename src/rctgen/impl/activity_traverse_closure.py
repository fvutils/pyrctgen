'''
Created on Jun 15, 2022

@author: mballance
'''
from rctgen.impl.ctor import Ctor


class ActivityTraverseClosure(object):
    
    def __init__(self, dt):
        self.traverse_t = dt
        pass
    
    def __call__(self, *args, **kwargs):
        print("__call__")
        return self
        pass
    
    def __enter__(self):
        ctor = Ctor.inst()
        ctor.push_expr_mode()
        c = ctor.ctxt().mkTypeConstraintScope()
        self.traverse_t.setWithC(c)
        
        ctor.push_constraint_scope(c)
        print("enter")
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        ctor = Ctor.inst()
        
        c = ctor.pop_constraint_scope()
        ctor.pop_expr_mode()
        
        pass