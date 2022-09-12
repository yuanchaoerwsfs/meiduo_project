import copy
import sys
class Dog():
    __i = None
    __name = None

    def __init__(self, name):
        if self.__name is None:
            self.name = name
            self.__name = name
        else:
            self.name = self.__name

    def __new__(cls, name):

        if cls.__i is None:
            print("父类初始化")
            cls.__i = object.__new__(cls)
            return cls.__i
        else:
            print('赋值初始化')
            return cls.__i


dog = Dog('dog')
print(dog.name)
print(id(dog))
cat = Dog('cat')
print(id(cat))
print(cat.name)

a=[11,22,33]
b=[]
b=a
c=copy.deepcopy(a)
d=copy.copy(a)
print(id(b))
print(id(a))
print(id(c))
print(id(d))

