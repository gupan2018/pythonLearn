# -*- coding:utf-8 -*-
# __author__ = 'gupan'
# 特点：先入先出
import queue

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

print(q.qsize())

# 使用get_nowwait()函数，如果队列里面没有数据会抛出异常queue.Empty
print(q.get_nowait())
q.get_nowait()
q.get_nowait()

# q.get()若队列里面没有数据，程序会卡住
# q.get()

# e.get()有两个参数，如果为空，则没有数据程序会卡住，
# 可以通过设置block=False来让程序不会阻塞
# 在设置了阻塞后，也可以设置timeout的数值，使程序在等待一段时间后抛出异常queue.Empty
# q.get(block=False)
# q.get(timeout=0.5)

# put函数也会卡住
# 当程序中设置了队列的最大长度后，队列满了以后会卡住
# k = queue.Queue(maxsize=1)
# k.put(1)
# k.put(2)

# 也可以和get一样，设置block和timeout参数，使程序抛出异常queue.Full
k = queue.Queue(maxsize=1)
k.put(1, block=False)
# k.put(2, block=False)
# k.put(2, timeout=0.5)
