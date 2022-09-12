def foo():
    print("hello foo")


print(foo.__name__)  # foo


def logged(func):
    def wrapper(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return wrapper


@logged
def cal(x):
    resul = x + x * x
    print(resul)


cal(2)
# 6
# cal was called
print(cal.__name__)  # wrapper
print(cal.__doc__)  # None
# 函数f被wrapper取代了，当然它的docstring，__name__就是变成了wrapper函数的信息了。
