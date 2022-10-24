
# https://blog.csdn.net/yjreset/article/details/79329979

def test(func):
    print('test')
    return func()

# 从这里可以看出@test等价于 test(xxx()),但是这种写法你得考虑python代码的执行顺序
@test
def xxx():
    print('hello world!')



