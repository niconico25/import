import sys
print('---')
print(__file__)
print(__name__)
print(__package__)
print(sys.path[0])

try:
    from . import module_a
    from . import sub_package
except ImportError:
    # attempted relative import
    # with no known parent package
    import module_a
    import sub_package
