import sys
print('---')
print(__file__)
print(__name__)
print(__package__)
print(sys.path[0])

try:
    from .. import module_a
except ValueError:
    # attempted relative import
    # beyond top-level package
    import module_a
