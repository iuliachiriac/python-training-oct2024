import math
import sys
from pprint import pprint

import legb
# from legb import X, my_func as outer_func
import pypackage.pymodule
# from pypackage import pymodule


print(math.pi, math.sqrt(9))
print(legb.X, legb.my_func(1))
# print(X, outer_func(1))

print("Special variables:",
      math.__name__, math.__file__, legb.__name__, legb.__file__)

pprint(sys.path)

print("After importing a package, names inside its __init__.py module can be "
      "accessed:", pypackage.py_init)

print(pypackage.pymodule.pyvar)
pypackage.pymodule.pyfunc()

# print(pymodule.pyvar)
# pymodule.pyfunc()
