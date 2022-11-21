import numpy as np
# https://blog.csdn.net/weixin_44350337/article/details/116034510
def print_with_name(var_in, name=None):
    print('----------------------------------------------------------')
    print("{} is:\n {}".format(name, var_in))
    print('----------------------------------------------------------')

def test_without_comma():
    arr = list(range(5))
    print_with_name(arr, "arr")
    print_with_name(arr[-1], "arr[-1]")
    print_with_name(arr[0:-1], "arr[0:-1]")
    print_with_name(arr[:-1], "arr[:-1]")
    print_with_name(arr[1:2], "arr[1:2]")
    print_with_name(arr[::-1], "arr[::-1]")
    print_with_name(arr[-1:0:-1], "arr[-1:0:-1]")
    print_with_name(arr[::-2], "arr[::-2]")
    print_with_name(arr[3::-1], "arr[3::-1]")


def test_with_comma():
    ndarr = np.random.rand(3, 4, 5)
    print_with_name(ndarr, "ndarr")
    print_with_name(ndarr[:, :, 0], "ndarr[:, :, 0]")
    print_with_name(ndarr[1:2, 1:3, 0], "ndarr[1:2, 1:3, 0]")
    print_with_name(ndarr[1:2, 1:3, 0:2], "ndarr[1:2, 1:3, 0:2]")
    # 我们将他放在中间a[: , ::-1 , :]，他就会把所有的第二层进行颠倒：
    print_with_name(ndarr[:, ::-1, :], "ndarr[:, ::-1, :]")
    pass

def test_with_ellippsis():
    ndarr = np.random.rand(3, 4, 5)
    print_with_name(ndarr[:, :, 0], "ndarr[:, :, 0]")
    print_with_name(ndarr[..., 0], "ndarr[..., 0]")
    print_with_name(ndarr[..., 0:2], "ndarr[..., 0:2]")
    # 是对最内层的列表进行逆序取值
    print_with_name(ndarr[..., ::-1], "ndarr[..., ::-1]")
 
if __name__ == '__main__':
    test_without_comma()
    test_with_comma()
    test_with_ellippsis()