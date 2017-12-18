# -*- coding:utf-8 -*-
# __author__ = 'gupan'
# 已经封装好了的协程

# 外部扩展包，需要安装gevent

# greenlet是手动切换协程，gevent封装了greenlet，是自动切换协程

from greenlet import greenlet

def test1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()

def test2():
    print(3)
    gr1.switch()
    print(4)
    # gr1.switch()

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
