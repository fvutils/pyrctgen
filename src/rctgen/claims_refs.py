'''
Created on Mar 19, 2022

@author: mballance
'''
from rctgen.impl.input_meta_t import InputMetaT
from rctgen.impl.output_meta_t import OutputMetaT


class input(metaclass=InputMetaT):
    pass

class output(metaclass=OutputMetaT):
    pass