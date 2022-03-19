# PyRctGen
Python modeling library for generating rule-based concurrent tests 
with a focus on hardware verifcation

PyRctGen uses an Action-Relation Level (ARL) modeling style consisting
of actions (that carry out work) related by:
- User-specified scheduling relationships
- User-specified dataflow relationships
- Inferred scheduling relationships
- Inferred dataflow relationships

The set of valid scheduling relationships can be limited by 
resources consumed by the actions.

PyRctGen borrows terminology from a variety of sources, including
UML, SystemVerilog, and Portable Stimulus. However, PyRctGen 
itself is none of these things. 

PyRctGen explores how an ARL modeling style can leverage Python notions
such as lambda functions, dynamic typing, and programmatic content
generation.

