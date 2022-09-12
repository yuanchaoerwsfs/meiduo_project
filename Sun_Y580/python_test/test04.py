import time


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        start_time = time.time()
        self._func()
        end_time = time.time()
        print('spend %s' % (end_time - start_time))


@Foo  # bar=Foo(bar)
def bar():
    print('bar')
    time.sleep(2)


bar()  # bar=Foo(bar)()>>>>>>>没有嵌套关系了,直接active Foo的 __call__方法