# -*- coding:utf-8 -*-
# __author__ = 'gupan'
# 存储数据时可以设置优先级

# put和get均有block和timeout参数

import queue
q = queue.PriorityQueue()
# put的参数是一个元祖，首位是优先级，末位是参数
q.put((10, 1))
q.put((9, 2))
q.put((11, 10))
q.put((-1, 4))

while not q.empty():
    print(q.get())