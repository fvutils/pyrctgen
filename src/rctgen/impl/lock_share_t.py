'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.ctor import Ctor
from rctgen.impl.ctor_scope import CtorScope
from rctgen.impl.field_claim_impl import FieldClaimImpl

class LockShareT(object):
    T = None
    IsLock = True
    
    def __init__(self, *args, **kwargs):
        raise Exception("LockShareT may not be created explicitly")
    
    @classmethod
    def createField(cls, name):
        ctor = Ctor.inst()
        s : CtorScope = ctor.scope()
        ret = FieldClaimImpl(
            name,
            s.lib_scope,
            cls.T._typeinfo)
        return ret
    
    