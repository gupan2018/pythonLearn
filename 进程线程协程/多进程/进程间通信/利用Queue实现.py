# -*- coding:utf-8 -*-
# __author__ = 'gupan'
from multiprocessing import Process, Queue


def func(q):
    q.put(1)


if __name__ == "__main__":
    q = Queue()
    # 父进程将自己的queue克隆了一份，交给了子进程，子进程向这个queue里面放了一个数据，
    # python将这个queue序列化了，放在了一个中间的地方，然后python再将这些数据反序列化
    # 给了父进程
    p = Process(target=func, args=(q, ))
    p.start()
    print(q.get())
