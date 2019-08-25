# PECO wrapper for python
A peco utility wrapper for peco command

## Examples

```
from pecowrappy import peco

ret = peco("""Apple
Orange
Banana""")
print(ret)

ret = peco(["Apple", "Orange", "Banana"])
print(ret)

ret = peco(range(5))
print(ret)
```
