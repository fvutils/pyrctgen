'''
Created on Mar 20, 2022

@author: mballance
'''
from enum import Enum, auto


class TypeKindE(Enum):
    Action = auto()
    Buffer = auto()
    Component = auto()
    Resource = auto()
    State = auto()
    Stream = auto()
    Struct = auto()
    