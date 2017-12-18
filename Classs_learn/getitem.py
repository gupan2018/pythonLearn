# -*- coding:utf-8 -*-
# __author__ = 'gupan'
class Foo(object):
    def __init__(self):
        self.__data = {}

    def __getitem__(self, item):
        return self.__data[item]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __delitem__(self, key):
        del self.__data[key]

t1 = Foo()
t1['name'] = "test01"
print(t1["name"])
del t1["name"]