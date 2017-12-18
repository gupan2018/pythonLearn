# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import threading
import time

def run(n):
    print("task", n)
    time.sleep(2)
    print("thread Done")

t1 = threading.Thread(target=run, args=("t1", ))
# 设置成守护线程必须要写在start()之前
t1.setDaemon(True)
t1.start()

