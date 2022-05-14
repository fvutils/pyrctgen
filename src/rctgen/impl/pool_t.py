'''
Created on May 12, 2022

@author: mballance
'''
from rctgen.impl.pool_size import PoolSize
from rctgen.impl.field_pool_impl import FieldPoolImpl
from rctgen.impl.ctor import Ctor
from rctgen.impl.ctor_scope import CtorScope

class PoolT(FieldPoolImpl):
    T = None
    
    def __init__(self, *args, **kwargs):
        raise Exception("Pool types may not be created explicitly")
    
    @classmethod
    def createField(cls, name):
        ctor = Ctor.inst()
        s : CtorScope = ctor.scope()
        ret = FieldPoolImpl(
            name,
            s.lib_scope,
            cls.T._typeinfo)
        
        return ret

    