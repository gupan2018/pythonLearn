# -*- coding:utf-8 -*-
# __author__ = 'gupan'
# list = [i * 2 for i in range(100000000)]
# print(list)

# gen = (i * 2 for i in range(100000000))
# print(gen.__next__())
# print(gen.__next__())
# for i in gen:
#     print(i)

#斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return "done"
gen = fib(10)
try:
    for i in range(1, 20):
        print(next(gen))
except StopIteration as e:
    print("\033[31;1mError is \033[0m", e)