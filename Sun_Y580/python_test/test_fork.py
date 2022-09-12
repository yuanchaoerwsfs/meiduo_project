import time
import os
from multiprocessing import Process


def test():
    while True:
        print("------test--------")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=test)  # 启动新的线程去执行test函数，并在内执行死循环
    p.start()
    # test()
    while True:  # 第二个线程执行下面死循环；证明有进程分别执行
        print("-----main-------")
        time.sleep(1)
