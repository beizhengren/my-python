from matplotlib.artist import get


class A:
    def __init__(self):
        self.__name = 'wyz'
        self.__age = 18
        pass
    # age
    def age(self):
        return self.__age
    #name
    @property#read only
    def name(self):
        return self.__name
    @name.setter # must be used with property
    def name(self, val):
        self.__name = val
    
    @name.getter
    def name(self):
        return self.__name
    @name.deleter
    def name(self):
        del self.__name

if __name__ == '__main__':
    a = A()
    print('--------------------------------')
    print(a.age())
    print(getattr(a, 'age'))
    print(hasattr(a, 'age'))
    print(a.age())
    print('--------------------------------')
    print("a.name is {}".format(getattr(a, 'name')) )
    
    setattr(a, 'name', 'heheda')
    print(a.name)
    del a.name  # print(a.name) will throw an error
    print('--------------------------------')

