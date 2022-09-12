def outer(func):
    print('enter outer', func)

    def wrapper():
        print('running outer')
        func()

    return wrapper


def inner(func):
    print('enter inner', func)

    def wrapper():
        print('running inner')
        func()

    return wrapper


@outer
@inner
def main():
    print('running main')


if __name__ == '__main__':
    main()

# 返回结果
# enter inner <function main at 0x000001A9F2BCDF28>
# enter outer <function inner.<locals>.wrapper at 0x000001A9F2BD5048>
# running outer
# running inner
# running main
