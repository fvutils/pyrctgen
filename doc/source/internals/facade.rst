User-Facade Operation
=====================


Type Decorators
---------------

Python classes to be treated as PyRctGen types are annotated with a decorator.
These decorators are evaluated during module loading, enabling the classes
to be registered with the PyRctGen system and allowing PyRctGen to perform
special processing.

Common Processing
^^^^^^^^^^^^^^^^^

- Implement dataclass fields by calling dataclasses.dataclass()
- Create core-library representation of containing type and typeinfo
- Process registered fields. Provide a validator?
- Capture exec blocks across the inheritance hierarchy. Provide a validator?

Type-Specific Processing: Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Field Declaration
-----------------