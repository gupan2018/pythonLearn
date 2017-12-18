# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import threading
import time

def run(n):
    print("test", n)
    print(threading.current_thread())
    time.sleep(2)

start_time = time.time()

t_objs = []
for i in range(50):
    test_num = "t_%s" % i
    t = threading.Thread(target=run, args=(test_num, ))
    t.start()
    t_objs.append(t)
    print("%s ended" % test_num)

print("当前活跃的线程个数", threading.active_count())

for obj in t_objs:
    obj.join()

print("the process cost %s", time.time() - start_time,
      threading.current_thread(),
      threading.active_count())
