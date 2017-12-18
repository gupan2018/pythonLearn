# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import threading
import time

def run():
    lock.acquire()
    global num
    num += 1
    lock.release()
    time.sleep(2)

lock = threading.Lock()

num = 0

t_objs = []

for i in range(600):
    t = threading.Thread(target=run, args=())
    t_objs.append(t)
    t.start()

time.sleep(3)

print(num)