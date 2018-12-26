# ~/import/relative/script/module_a.py
import sys
print('---')
print(sys.path[0])
print(__file__)
print(__package__)
print(__name__)

try:
    from .sub_package import module_b
except ImportError:
    # attempted relative import
    # with no known parent package
    import sub_package.module_b
