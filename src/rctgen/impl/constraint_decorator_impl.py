'''
Created on Jun 2, 2022

@author: mballance
'''
from rctgen.impl.constraint_impl import ConstraintImpl
from rctgen.impl.ctor import Ctor

class ConstraintDecoratorImpl(object):
    
    def __init__(self, kwargs):
        pass
    
    def __call__(self, T):
        impl = ConstraintImpl(T.__name__, T)
        Ctor.inst().push_constraint_decl(impl)
    