'''
Created on Apr 30, 2022

@author: mballance
'''
from rctgen.impl.ctor import Ctor
import libvsc.core as vsc
from rctgen.impl.activity_traverse_closure import ActivityTraverseClosure

class DoImplMeta(type):

    def __init__(self, name, bases, dct):
        pass
        
    def __getitem__(self, item):
        ctor = Ctor.inst()
        print("DoImplMeta: %s" % str(item._typeinfo._lib_obj))
        
        # Add a field declaration to the activity scope
        field_t = ctor.ctxt().mkTypeFieldPhy(
            "__tmp__",
            item._typeinfo._lib_obj,
            False,
            vsc.TypeFieldAttr.NoAttr,
            None)
        
        ctor.activity_scope().addField(field_t)

        target = ctor.ctxt().mkTypeExprFieldRef()
        target.addRootRef()
        target.addIdxRef(field_t.getIndex())
                
        dt_traverse = ctor.ctxt().mkDataTypeActivityTraverse(
            target,
            None)
        
        ctor.activity_scope().addActivity(dt_traverse)
        
        # Add a traversal statement to the current activity scope
        return ActivityTraverseClosure(dt_traverse)
    