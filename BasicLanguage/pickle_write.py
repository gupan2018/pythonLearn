# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import pickle
def sayhi(name):
    print("hello,", name)

info = {
    'name':'gupan',
    'age':22,
    'func':sayhi
}

with open("test.txt", "wb") as f_w:
    f_w.write(pickle.dumps(info))