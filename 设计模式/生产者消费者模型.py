# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import threading, time, queue

def Comsumer(name):
    while True:
        print(name, "eat", q.get())
        time.sleep(1)

def Productor():
    count = 0
    while True:
        q.put("骨头%s" % count)
        print("制造了骨头%s" % count)
        count += 1
        time.sleep(0.1)

q = queue.Queue(maxsize=10)
p1 = threading.Thread(target=Productor,)
c1 = threading.Thread(target=Comsumer, args=("CRH", ))
c2 = threading.Thread(target=Comsumer, args=("LHY", ))

p1.start()
c1.start()
c2.start()






