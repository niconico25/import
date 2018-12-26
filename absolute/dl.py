import sys


def exe():
    del sys.modules['package']
    del sys.modules['package.module_a']
    del sys.modules['package.sub_package']
    del sys.modules['package.sub_package.module_b']
