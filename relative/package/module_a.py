# ~/import/relative/package/module_a.py
import sys
print('---')
print(sys.path[0])
print(__file__)
print(__package__)
print(__name__)

from .sub_package import module_b
