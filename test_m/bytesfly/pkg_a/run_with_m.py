'''
    # python -m bytesfly.pkg_a.run
    add cwd in sys.path
    for example, "/home/wyz/workspace/projects/my-python/test_m"
'''
import sys
# pkg_a
# import module
from bytesfly.pkg_a import module_a1
# import function directly. must add relevant dir '.'
from .module_a1 import bar
# include module
import bytesfly.pkg_a.module_a1

# pkg_b
from bytesfly.pkg_b import modlule_b1
from ..pkg_b import modlule_b1
import bytesfly.pkg_b.modlule_b1

from ..pkg_b.modlule_b1 import bar


print(sys.path)

if __name__ == '__main__':
    # module in pkg a
    module_a1.foo()
    bar()
    bytesfly.pkg_a.module_a1.baz()
    print('---------------------------')

    # module in pkg b
    modlule_b1.foo()
    bar()


    