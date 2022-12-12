'''
    # python -m bytesfly.pkg_a.run
    add cwd in sys.path
    for example, "/home/wyz/workspace/projects/my-python/test_m"
'''
import sys
# pkg_a
# import module
# from bytesfly.pkg_a import module_a1
# import function directly. must add relevant dir '.'
# from .module_a1 import bar
# include module
sys.path.append("/home/wyz/workspace/projects/my-python/test_m")
# import bytesfly.pkg_a.module_a1
from bytesfly.pkg_a import module_a1
print(sys.path)
import module_a2
if __name__ == '__main__':
    ## module in pkg a
    module_a1.foo()
    # bar()
    # bytesfly.pkg_a.module_a1.baz()
    print('---------------------------')

    module_a2.bar()

    