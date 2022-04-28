'''
Created on Apr 27, 2022

@author: mballance
'''

class FieldModelInfo(object):
    
    def __init__(self, facade_obj, name):
        self._facade_obj = facade_obj
        self._name = name
        self._lib_obj = None