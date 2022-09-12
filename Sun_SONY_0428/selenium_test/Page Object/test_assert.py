from time import sleep
# 功能:计算a+b
def add(a, b):
    sleep(5)
    return a + b


# 功能：用于判断素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            sleep(5)
            return False
        return True


# 测试相等
def test_add_1():
    sleep(5)
    assert add(3, 4) == 7


# 测试不相等
def test_add_2():
    assert add(17, 22) != 50


# 测试大于或等于
def test_add_3():
    assert add(17, 22) <= 50


# 测试小于或等于
def test_add_4():
    assert add(2, 22) >= 50


# 测试包含
def test_in():
    a = 'hello'
    b = 'he'
    assert b in a


# 测试不包含
def test_not_in():
    a = 'hello'
    b = 'hi'
    assert b not in a


# 判断是否为ture
def test_ture_1():
    assert is_prime(13)


# 判断是否为ture
def test_ture_2():
    assert is_prime(7) is True


# 判断是否不为ture
def test_ture_3():
    assert not is_prime(4)


# 判断是否不为ture
def test_ture_4():
    assert not is_prime(6) is not True


# 判断是否为true
def test_false_5():
    assert is_prime(8) is False
