def selfAdd(a):
    """自增"""
    a += a
    print(a)


a_int = 1
selfAdd(a_int)
a_list = [1, 2]

selfAdd(a_list)
A = a_list = a_list
print(A)

sum = lambda arg1, arg2: arg1 + arg2

print(sum(20, 30))

import time


class Animal(object):

    # 初始化方法
    # 创建完对象后会自动被调用
    def __init__(self, name):
        print('__init__方法被调用')
        self.__name = name

    # 析构方法
    # 当对象被删除时，会自动被调用
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉了..." % self.__name)


# 创建对象
dog = Animal("哈皮狗")

# 删除对象
del dog

cat = Animal("波斯猫")
cat2 = cat
cat3 = cat

print("---马上 删除cat对象")
del cat
print("---马上 删除cat2对象")
del cat2
print("---马上 删除cat3对象")
del cat3

print("程序2秒钟后结束")
time.sleep(2)


class base(object):
    def test(self):
        print('----base test----')
class A(base):
    def test(self):
        print('----A test----')

# 定义一个父类
class B(base):
    def test(self):
        print('----B test----')

# 定义一个子类，继承自A、B
class C(A,B):
    pass


obj_C = C()
obj_C.test()
print(C.__mro__)

#coding=utf-8
class Cat(object):
    def __init__(self,name):
        self.name = name
        self.color = 'yellow'


class Bosi(Cat):

    def __init__(self,name):
        # 调用父类的__init__方法1(python2)
        #Cat.__init__(self,name)
        # 调用父类的__init__方法2
        #super(Bosi,self).__init__(name)
        # 调用父类的__init__方法3
        super().__init__(name)

    def getName(self):
        return self.name

bosi = Bosi('xiaohua')

print(bosi.name)
print(bosi.color)


class People(object):
    address = '山东' #类属性
    def __init__(self):
        self.name = 'xiaowang' #实例属性
        self.age = 20 #实例属性

p = People()
p.age =12 #实例属性
print(p.address) #正确
print(p.name)    #正确
print(p.age)     #正确