# ~/import/relative/script/__main__.py
import sys
print('---')
print(sys.path[0])
print(__file__)
print(__package__)
print(__name__)

try:
    from . import module_a
    from . import sub_package
except ImportError:
    # attempted relative import
    # with no known parent package
    import module_a
    import sub_package
