# ~/import/absolute/script/sub_package/module_b.py
import sys
print('---')
print(sys.path[0])
print(__file__)
print(__package__)
print(__name__)

import module_a
