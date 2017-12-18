# -*- coding:utf-8 -*-
# __author__ = 'gupan'
__author__ = "Alex Li"
#
# import time
# def consumer(name):
#     print("%s 准备吃包子啦!" %name)
#     while True:
#        baozi = yield "gupan"
#
#        print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
#
# c = consumer("ChenRonghua")
# c.__next__()
#
# def producer(name):
#     c = consumer('A')
#     c2 = consumer('B')
#     c.__next__()
#     c2.__next__()
#     print("老子开始准备做包子啦!")
#     for i in range(10):
#         time.sleep(1)
#         print("做了1个包子,分两半!")
#         c.send(i)
#         c2.send(i)
#
# producer("alex")

# from collections import Iterable
#
# print(isinstance([], Iterable))

#  from collections import Iterator
# print(isinstance([], Iterator))
# print(isinstance((x for x in range(10)), Iterator))

# from collections import Iterator
# a = [1, 2, 3]
# print(isinstance(a, Iterator))
# #iter(a)
# a = iter(a)
# print(isinstance(a, Iterator))
# print(a.__next__())