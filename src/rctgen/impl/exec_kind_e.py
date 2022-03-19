'''
Created on Mar 19, 2022

@author: mballance
'''
from enum import Enum, auto


class ExecKindE(Enum):
    Body = auto()
    PreSolve = auto()
    PostSolve = auto()
    InitDown = auto()
    InitUp = auto()