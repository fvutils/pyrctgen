'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.activity_block_meta_t import ActivityBlockMetaT
from rctgen.impl.do_impl_meta import DoImplMeta
from rctgen.impl.do_with_impl_meta import DoWithImplMeta


class parallel(metaclass=ActivityBlockMetaT):
    
    def __init__(self, *args, **kwargs):
        pass
    
    def __enter__(self):
        print("parallel.__enter__")
        
    def __exit__(self, t, v, tb):
        pass
    
class sequence(metaclass=ActivityBlockMetaT):
    def __init__(self, *args, **kwargs):
        pass
    
    def __enter__(self):
        print("sequence.__enter__")
        
    def __exit__(self, t, v, tb):
        pass
    
class schedule(metaclass=ActivityBlockMetaT):
    def __init__(self, *args, **kwargs):
        pass
    
    def __enter__(self):
        print("sequence.__enter__")
        
    def __exit__(self, t, v, tb):
        pass

class match(object):
    
    def __init__(self, expr):
        pass
    
    def __enter__(self):
        print("sequence.__enter__")
        
    def __exit__(self, t, v, tb):
        pass

class do(metaclass=DoImplMeta):
    pass

class do_with(metaclass=DoWithImplMeta):
    pass
    
