# A Sort of Working CircuirPython Debugger
CircuitPython does not support Python's `pdb` debugger,
so I came up with this library for line-by-line debugging.
It is a very coarse implementation.
You might find it helpful but far from powerful.

It currently can
- Run code on `code.py` file line-by-line
- Run debugging commands in the middle
- Check global variables
- Skip comments and white lines in the source code
- Single breakpoints

It cannot
- Show function local variables
    - This is due to [micropython's design](https://github.com/micropython/micropython/wiki/Differences#differences-by-design)

I am also working on
- jumping in and out of indentions
# How to use
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/gas35_1G3Fg/0.jpg)](https://www.youtube.com/watch?v=gas35_1G3Fg)

# Example 1
Debug the whole code
``` python
import debug
def addone(a):
    b = a + 1
    return b
    
a = 1
for i in range(3):
    a = addone(a)
```

# Example 2
One breakpoint
``` python
from debugfun import breakpoint, vars
def addone(a):
    b = a + 1
    return b
    
a = 1
for i in range(3):
    a = addone(a)
    breakpoint()
```