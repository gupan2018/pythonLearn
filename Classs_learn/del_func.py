# -*- coding:utf-8 -*-
# __author__ = 'gupan'
# class Xigou:
#     def __init__(self):
#         print("Xigou1 construct")
#
#     def __del__(self):
#         print("Xigou disconstruct")
#
# Xigou()

class Xigou:
    def __init__(self):
        print("Xigou1 construct")

    def __del__(self):
        print("Xigou disconstruct")

t1 = Xigou()
print("干点其他事")
del t1
print("再干点其他事")