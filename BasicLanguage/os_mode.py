# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import os
cmd_res = os.popen("dir")
print(cmd_res.read())