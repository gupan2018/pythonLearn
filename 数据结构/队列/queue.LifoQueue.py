# -*- coding:utf-8 -*-
# __author__ = 'gupan'
# 特点：后入先出
# 和queue.Queue一样，都有block和timeout等参数
import queue

q = queue.LifoQueue()

q.put(1)
q.put(2)
q.put(3)

while not q.empty():
    print(q.get())