'''
Created on Apr 4, 2022

@author: mballance
'''
import dataclasses
from rctgen.impl.ctor import Ctor
from rctgen.impl.type_info import TypeInfo


class DecoratorImplBase(object):
    
    def init(self, T, typeinfo):
        Tp = dataclasses.dataclass(T, init=False)

        setattr(Tp, "_typeinfo", typeinfo)
        
        print("RandClass %s" % str(T))
#        Tp._is_randclass = True
#        Tp._typeinfo = RandClassTypeInfo()
        
        print("  Bases: %s" % str(T.__bases__))
        
        constraints = Ctor.inst().pop_constraint_decl()
        Tp._typeinfo._constraint_l.extend(constraints)
        
        for c in constraints:
            Tp._typeinfo._constraint_m[c._name] = c
            
        for b in T.__bases__:
            if hasattr(b, "_typeinfo"):
                self.__collectConstraints(Tp._typeinfo, b)
                
        return Tp        
    
    def populate_execs(self, ti : TypeInfo, supported_s):
        execs = Ctor.inst().pop_exec_types()
        
        for e in execs:
            print("Exec: %s" % str(e.kind))
            if e.kind not in supported_s:
                raise Exception("Unsupported exec kind %s" % str(e.kind))
            if e.kind in ti._exec_m.keys():
                ti._exec_m[e.kind].append(e)
            else:
                ti._exec_m[e.kind] = [e]
