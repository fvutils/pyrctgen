'''
Created on Mar 19, 2022

@author: mballance
'''
from enum import Enum, auto

class StructKindE(Enum):
    Buffer = auto()
    Resource = auto()
    State = auto()
    Stream = auto()
    Struct = auto()
    
    