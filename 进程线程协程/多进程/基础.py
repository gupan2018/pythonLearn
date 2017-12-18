# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import multiprocessing
import time

def run(n):
    print("start", n)
    time.sleep(10)


if __name__ == "__main__":
    start_time = time.time()
    for i in range(10):
        p = multiprocessing.Process(target=run, args=(i,))
        p.start()

    use_time = time.time() - start_time
    print(use_time)