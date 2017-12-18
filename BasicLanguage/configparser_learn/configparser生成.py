# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import configparser

# conf = configparser.ConfigParser()
# conf["info"] = {
#     "name" : "gupan",
#     "age" : 24
# }
#
# conf["connect"] = {}
# cnn = conf["connect"]
# cnn["Host"] = "192.168.17.133"
# conf["connect"]["Port"] = "8888"
#
# with open("example.conf", "w") as confile:
#     conf.write(confile)

conf = configparser.ConfigParser()
conf.read("example.ini")
conf.remove_section("connect")
conf.remove_option("info", "age")
with open("example2.ini", "w") as confile:
    conf.write(confile)
