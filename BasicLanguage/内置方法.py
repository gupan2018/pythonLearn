# -*- coding:utf-8 -*-
# __author__ = 'gupan'

# print(all([1, 2, 3, 0]))
# print(all([1, 2, 3]))

# print(ascii(["顾攀", 2]))
# print(type(ascii(["顾攀", 2])))

# str = "abcidonods"
# str[0] = 'c'
# print(str)

# b = bytearray("abcde", encoding = "utf-8")
# b[0] = 100
# print(b)

# def test():pass
#
# print(callable([]))
# print(callable(test))

# print(chr(100))
#
# print(ord("1"))
# code = "1+3/2*6"
# c = compile(code, '', "exec")
# exec(c)

# res = filter(lambda n:n>5, range(10))#过滤出range(10)中，>5的数据
# for i in res:
#     print(i)
#
# res = map(lambda n:n>5, range(10))#判断range(10)中的元素是否大于5，大于5返回True，小于等于5返回True
# for i in res:
#     print(i)
# import functools
# res = functools.reduce(lambda x, y:x + y, range(10))
# print(res)
#
# print(globals())

# a = [1,2,3,4]
# b=["a", "b", "c", "d"]
# for i in zip(a, b):
#     print(i)