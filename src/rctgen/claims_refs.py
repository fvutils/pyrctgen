'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.input_meta_t import InputMetaT
from rctgen.impl.output_meta_t import OutputMetaT
from rctgen.impl.lock_meta_t import LockMetaT
from rctgen.impl.share_meta_t import ShareMetaT
from rctgen.impl.pool_meta_t import PoolMetaT


class input(metaclass=InputMetaT):
    pass

class output(metaclass=OutputMetaT):
    pass

class lock(metaclass=LockMetaT):
    pass

class share(metaclass=ShareMetaT):
    pass

class pool(metaclass=PoolMetaT):
    pass