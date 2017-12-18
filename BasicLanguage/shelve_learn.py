# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import shelve
#
# a = shelve.open("test1114")
# class Test:
#     def __init__(self, n):
#         self.n = n
#
# dic = {"name":"gupan", "age":12}
# list = [1, 2, 3]
#
# t1 = Test(1)
# t2 = Test(2)
#
# a["test1"] = t1
# a["test2"] = t2
# a["dic"] = dic
# a["list"] = list
# a.close()

a = shelve.open("test1114")
print(a.get("dic"))
print(a.get("list"))
#print(a["dic"])
a.close()