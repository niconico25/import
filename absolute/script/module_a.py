# ~/import/absolute/script/module_a.py
import sys
print('---')
print(sys.path[0])
print(__file__)
print(__package__)
print(__name__)

import sub_package.module_b
