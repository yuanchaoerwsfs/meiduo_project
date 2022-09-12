import time


# 遵守开放封闭原则
def foo():
    start = time.time()
    print(start)  # 1504698634.0291758从1970年1月1号到现在的秒数，那年Unix诞生
    time.sleep(3)
    end = time.time()
    print('spend %s' % (end - start))


foo()


class A(object):
    def __init__(self):
        print("这是 init 方法")

    def __new__(cls):
        print("这是 new 方法")
        return object.__new__(cls)


test=A()
test.a=100
print(test.a)
