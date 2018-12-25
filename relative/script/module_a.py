import sys
print('---')
print(__file__)
print(__name__)
print(__package__)
print(sys.path[0])

try:
    from .sub_package import module_b
except ImportError:
    # attempted relative import
    # with no known parent package
    import sub_package.module_b
