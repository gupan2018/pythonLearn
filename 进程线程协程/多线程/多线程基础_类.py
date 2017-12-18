# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    # 必须是run
    def run(self):
        print("task", self.n)
        time.sleep(2)


t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()
t2.start()