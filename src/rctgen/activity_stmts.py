'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.activity_block_meta_t import ActivityBlockMetaT


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
    
