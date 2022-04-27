'''
Created on Apr 26, 2022

@author: mballance
'''

from .impl.bit_t_meta import BitTMeta
from .impl.int_t_meta import IntTMeta
from .impl.scalar_t import ScalarT
from .impl.enum_t import EnumT
from .impl.enum_t_meta import EnumTMeta
from .impl.rand_t import RandT
from .impl.rand_t_meta import RandTMeta


class rand(RandT, metaclass=RandTMeta):
    pass

class enum_t(EnumT, metaclass=EnumTMeta):
    pass

class int_t(ScalarT, metaclass=IntTMeta):
    W = 32
    S = True
    
    
class bit_t(ScalarT, metaclass=BitTMeta):
    W = 1
    S = False
    pass

#********************************************************************
#* Convenience types
#********************************************************************
uint8_t = bit_t[8]
uint16_t = bit_t[16]
uint32_t = bit_t[32]
uint64_t = bit_t[64]

rand_uint8_t = rand[bit_t[8]]
rand_uint16_t = rand[bit_t[16]]
rand_uint32_t = rand[bit_t[32]]
rand_uint64_t = rand[bit_t[64]]

int8_t = int_t[8]
int16_t = int_t[16]
int32_t = int_t[32]
int64_t = int_t[64]

rand_int8_t = rand[int_t[8]]
rand_int16_t = rand[int_t[16]]
rand_int32_t = rand[int_t[32]]
rand_int64_t = rand[int_t[64]]
