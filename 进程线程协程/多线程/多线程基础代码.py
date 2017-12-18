# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import threading
import time

def run(n):
    print("Task, ", n)
    time.sleep(2)

t1 = threading.Thread(target=run, args=("t1",))
t2 = threading.Thread(target=run, args=("t2",))

t1.start()
t2.start()