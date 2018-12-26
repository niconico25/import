# ~/relative/package/__init__.py
import sys
print('---')
print(sys.path[0])
print(__file__)
print(__package__)
print(__name__)

from . import module_a
from . import sub_package
