# ~/import/relative/script/sub_package/module_b.py
import sys
print('---')
print(sys.path[0])
print(__file__)
print(__package__)
print(__name__)

try:
    from .. import module_a
except ValueError:
    # attempted relative import
    # beyond top-level package
    import module_a
