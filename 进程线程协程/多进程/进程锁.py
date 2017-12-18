# -*- coding:utf-8 -*-
# __author__ = 'gupan'
# 进程之间为什么会需要进程锁
# 屏幕共享时，保证打印数据不会乱，即一个进程打印数据时不会在中途有其他数据插进来
from multiprocessing import Lock
import multiprocessing


def run_test(lock, i):
    lock.acquire()
    print("Hello World", i)
    lock.release()


if __name__ == "__main__":
    lock = Lock()

    for i in range(10):
        p = multiprocessing.Process(target=run_test, args=(lock, i))
        p.start()