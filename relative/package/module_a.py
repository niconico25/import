import sys
print('---')
print(__file__)
print(__name__)
print(__package__)
print(sys.path[0])

from .sub_package import module_b
