# -*- coding:utf-8 -*-
# __author__ = 'gupan'
from multiprocessing import Process, Lock
import queue


def func(q):
    lock.acquire()
    q.put(1)
    lock.release()


if __name__ == "__main__":
    lock = Lock()
    q = queue.Queue()
    p = Process(target=func, args=(q, ))
    p.start()
    print(q.get())