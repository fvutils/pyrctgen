'''
Created on Apr 30, 2022

@author: mballance
'''
from rctgen.impl.ctor import Ctor
import libvsc.core as vsc

class DoImplMeta(type):

    def __init__(self, name, bases, dct):
        pass
        
    def __getitem__(self, item):
        ctor = Ctor.inst()
        print("DoImplMeta: %s" % str(item._typeinfo._lib_obj))
        
        # Add a field declaration to the action
        field_t = ctor.ctxt().mkTypeFieldPhy(
            "__tmp__",
            item._typeinfo._lib_obj,
            False,
            vsc.TypeFieldAttr.NoAttr,
            None)
        
        # Add a traversal statement to the current activity scope
        pass
    