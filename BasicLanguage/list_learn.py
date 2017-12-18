# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import copy
names_1 = ["gupan", "duoduo", "bingbing", "shaojie",["buyu", "ziyi"]]
names_2 = copy.deepcopy(names_1)
names_1[0] = "顾攀"
print("names_1:", names_1)
print("names_2:", names_2)

names_1[-1][0] = "不与"
print("names_1:", names_1)
print("names_2:", names_2)

str1 = "gupan"
str2 = str1
str1 = "mod"
print("str1:", str1 + "\n" + "str2:", str2)