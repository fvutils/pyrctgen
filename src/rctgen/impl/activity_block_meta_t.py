'''
Created on Mar 19, 2022

@author: mballance
'''

class ActivityBlockMetaT(type):
    
    def __init__(self, name, bases, dct):
        pass

    def __enter__(self):
        print("ActivityBlockMetaT.__enter__")
        
    def __exit__(self, t, v, tb):
        pass    
    
    