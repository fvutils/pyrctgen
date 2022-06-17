

Actions are traversed in one of two fundamental ways:
- By handle
- By type

Each of these key variants supports two sub-variants
- With parameters
- With constraints

All six combinations are possible and legal.

By-handle traversals are specified by referencing the 
handle in the body of the activity:

```
  def activity(self):
    self.a
```

By-type traversals are specified by referencing the
type via 'rg.do':

```
  def activity(self):
    rg.do[Top.A]
```

