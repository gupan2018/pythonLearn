# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import optparse

# 不显示usage部分
parse = optparse.OptionParser(
    usage=optparse.SUPPRESS_USAGE,
    prog="cmdtest",
    version="%prog 1.0",
    description="this is for cmd test")
parse.add_option("-p", "--parameter", nargs=2, type="int")
(option, args) = parse.parse_args()
print("option:", option)
print("args:", args)
# print(type(option.parameter[0]))