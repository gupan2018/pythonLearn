# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import gevent


def test1():
    print(1)
    gevent.sleep(2)
    print(2)


def test2():
    print(3)
    gevent.sleep(1)
    print(4)


def test3():
    print(5)
    gevent.sleep(0)
    print(6)


if __name__ == "__main__":
    gevent.joinall([
        gevent.spawn(test1),
        gevent.spawn(test2),
        gevent.spawn(test3)
    ])