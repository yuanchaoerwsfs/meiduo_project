import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name='Sun'):
        super().__init__()
        self.name = name

    def getName(self):
        print(self.name)
        time.sleep(2)


if __name__ == '__main__':
    # 启动线程1
    thread_01 = MyThread()
    # 启动线程2
    thread_02 = MyThread('fan')

    thread_01.start()
    thread_02.start()
    thread_01.getName()
    thread_02.getName()