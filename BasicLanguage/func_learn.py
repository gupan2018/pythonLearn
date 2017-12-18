# -*- coding:utf-8 -*-
# __author__ = 'gupan'

def test(*args):
    print(args)

test(1, 2, 3,4, 5)
test(*[1, 2, 3])


def test01(x, *args):
    print(x)
    print(args)
test01("gupan", "xi", "huan", "xue", "xi")

def test02(**args):
    print(args)

test02(name="gupan", age=12)
test02(**{"name":"gupan", "age":12})

# def test02(name, age, **args):
#     print(name)
#     print(age)
#     print(args)

# test02("a", 12, name="gupan", age=12)

# name = "gupan"
# print(name)
#
# def testglobal():
#     global name
#     name = "huangli"
# testglobal()
# print(name)
#
# def test():
#     global name
#     name = "gupan"
# test()
# print(name)

def add(a, b):
    return a + b

def test(x, y, f):
    sum = x + y + f(x, y)
    return sum

print(test(1, 2, add))

import re

print(re.findall("\.\.", "cusin..cisa..ncjisa..ncisa..cius"))

print("chuiewb/".split("/"))

list = ["cnuds", "nucis", ""]
list.remove("")
print(list)

path = "cnjs/ncis/ncis/csin/csdc"
print("------------------")
print(re.search("/*$", path).group())