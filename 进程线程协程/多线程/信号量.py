# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import threading, time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    lock.acquire()
    print("run the thread: %s\n" % n)
    lock.release()
    semaphore.release()
    # print("\033[33;1mJust for test\033[0m", n)

if __name__ == '__main__':
    lock = threading.Lock()
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('----all threads done---')