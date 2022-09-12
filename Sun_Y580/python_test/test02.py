import time


def show_time(f):
    def inner1():
        start = time.time()
        f()
        end = time.time()
        print('spend1 %s' % (end - start))

    return inner1


def show_time1(f):
    def inner1():
        start = time.time()
        f()
        end = time.time()
        print('spend2 %s' % (end - start))

    return inner1


@show_time  # foo=show_time(f)
@show_time1  # foo=show_time(f)
def foo():
    print('foo...')
    time.sleep(1)


if __name__ == '__main__':
    foo()
