# ~/import/absolute/package/sub_package/__init__.py
import sys
print('---')
print(sys.path[0])
print(__file__)
print(__package__)
print(__name__)

import package.sub_package.module_b
