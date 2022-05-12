'''
Created on Apr 30, 2022

@author: mballance
'''

class DoWithImpl(object):
    
    def __enter__(self):
        print("__enter__")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")