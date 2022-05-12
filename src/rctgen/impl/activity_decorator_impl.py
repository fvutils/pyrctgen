'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.ctor import Ctor
from rctgen.impl.activity_decl import ActivityDecl

class ActivityDecoratorImpl(object):

    def __init__(self, kwargs):
        pass
    
    def __call__(self, T):
        Ctor.inst().push_activity_decl(ActivityDecl(T))
        return T
        