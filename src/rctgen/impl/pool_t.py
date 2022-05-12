'''
Created on May 12, 2022

@author: mballance
'''
from rctgen.impl.pool_size import PoolSize

class PoolT(object):
    T = None
    
    def __init__(self, *args, **kwargs):
        raise Exception("Pool types may not be created explicitly")
    