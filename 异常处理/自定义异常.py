# -*- coding:utf-8 -*-
# __author__ = 'gupan'

class GpError(Exception):
    def __init__(self, msg):
        self.msg = msg

try:
    raise GpError('这是一个测试中的错误')
except GpError as e:
    print(e)
