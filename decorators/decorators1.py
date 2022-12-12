
# # https://blog.csdn.net/yjreset/article/details/79329979

# def test(func):
#     print('test')
#     return func()

# # 从这里可以看出@test等价于 test(xxx()),但是这种写法你得考虑python代码的执行顺序
# @test
# def xxx():
#     print('hello world!')

# https://www.geeksforgeeks.org/python-functools-wraps-function/
def a_decorator(func):
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        # Extend some capabilities of func
        func()
    return wrapper
 # add @, __name__ and __doc__ will be the wrapping fucntion, such as a_decorator
 # remove @, vice versa.
#@a_decorator
def first_function():
    """This is docstring for first function"""
    print("first function")
 
@a_decorator
def second_function(a):
    """This is docstring for second function"""
    print("second function")
 
# print(first_function.__name__)
# print(first_function.__doc__)
# print(second_function.__name__)
# print(second_function.__doc__)

help(first_function)
help(second_function)