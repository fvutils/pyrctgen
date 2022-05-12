'''
Created on May 8, 2022

@author: mballance
'''

class ActivityDecl(object):
    
    def __init__(self, activity_f):
        self._activity_f = activity_f
        
    @property
    def activity_f(self):
        return self._activity_f
    