# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import pickle
def sayhi(name):
    print("my name is,", name)

with open("test.txt", "rb") as f_r:
    data = pickle.load(f_r)

data["func"](data["name"])