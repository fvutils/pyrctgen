'''
Created on May 8, 2022

@author: mballance
'''
from rctgen.impl.type_info import TypeInfo
from rctgen.impl.type_kind_e import TypeKindE
from rctgen.impl.ctor import Ctor
import typing

class TypeInfoAction(TypeInfo):
    
    def __init__(self, Tp):
        super().__init__(Tp, TypeKindE.Action)
        self._activity_decl_l = []
        self._component_t = None
        
    def addActivityDecl(self, a):
        self._activity_decl_l.append(a)
        
    def elab(self):
        if self._is_elab:
            return
        
        ctor = Ctor.inst()
        
        self._elabFields()

        ctor.push_scope(None, self.lib_obj, True)
        obj = self._Tp()
        
        # Elaboate constraints
        ctor.push_expr_mode()
        for c in self._constraint_l:
            constraint = ctor.ctxt().mkTypeConstraintBlock(c.name)
            ctor.push_constraint_scope(constraint)
            c.func(obj)
            ctor.pop_constraint_scope()
            self.lib_obj.addConstraint(constraint)
        ctor.pop_expr_mode()

        ctor.push_activity_mode()
        for a in self._activity_decl_l:
            activity_s = ctor.ctxt().mkDataTypeActivitySequence()
            activity_f = ctor.ctxt().mkTypeFieldActivity(
                    "activity",
                    activity_s,
                    True)
            self.lib_obj.addActivity(activity_f)
            print("activity index=%d" % activity_f.getIndex())
            
            ctor.push_activity_scope(activity_s)
            print("--> activity")
            a.func(obj)
            print("<-- activity")
            ctor.pop_activity_scope()
        ctor.pop_activity_mode()
            
        ctor.pop_scope()
                
        self._is_elab = True
        
    