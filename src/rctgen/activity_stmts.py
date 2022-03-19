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