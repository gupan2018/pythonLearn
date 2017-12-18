# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import os

# print(__file__)
# print(os.path.dirname(__file__) + "/byte2str.py")
# wb = open(os.path.dirname(__file__) + "\\test01.txt", "r")
# wb.read()
# wb.close()


# print(os.popen("dir").read())
#
# print(os.path.basename("c:/cdw/cdsac/fdsads/csa.yxyxy"))

# import socketserver
#
# socketserver.TCPServer
# socketserver.UDPServer
#
# import sys
# import time
# for i in range(101):
#     s1 = "\r[%s%s]%d%%"%("*"*i," "*(100-i),i)
#     sys.stdout.write(s1)
#     sys.stdout.flush()
#     time.sleep(0.3)

import hashlib
# import json
#
# sha_handle = hashlib.sha256()
# sha_handle.update(b"abc")
# test_dic = {
#     "sha_obj":sha_handle,
#     "filename":"test"
# }
#
# # # sha_handle.update(b"abc")
# # for i in dir(sha_handle):
# #     print(i)
#
# json_str = json.dumps(test_dic)
# json_dic = json.loads(json_str)

# print(sha_handle.name)

# print(sha_handle.copy())

import unittest
import time


class MyTest(unittest.TestCase):
    def test_1(self):
        print("in the test_1")
        time.sleep(2)
        print("test_1 end")

    def test_2(self):
        print("in the test_2")
        print("test_2 end")


