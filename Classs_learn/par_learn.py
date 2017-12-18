# -*- coding:utf-8 -*-
# __author__ = 'gupan'

# class Class_test:
#     class_par = 123
#     def __init__(self):
#         pass
# print(Class_test.class_par)
#
# t1 = Class_test()
# t2 = Class_test()
# t1.class_par = 234
#
# print("t1:", t1.class_par)
# print("t2:", t2.class_par)
# print("Class_test:", Class_test.class_par)

class Person01(object):
    country = "中国"
    def __init__(self):
        pass

class Person02:
    def __init__(self, country):
        self.country = country
        pass



