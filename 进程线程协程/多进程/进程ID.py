# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import os
import multiprocessing

# 获取进程ID
print("process ID:", os.getpid())

# 获取父进程ID
print("parent ID:", os.getppid())