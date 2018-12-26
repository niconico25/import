# ~/import/absolute/script/__main__.py
import sys
print('---')
print(sys.path[0])
print(__file__)
print(__package__)
print(__name__)

import module_a
import sub_package
