# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import multiprocessing, os
from multiprocessing import Manager


# manager自己内部已经加了锁，不允许两个进程同时修改一份数据

def run(d, l):
    d[os.getppid()] = os.getppid()
    l.append(os.getppid())
    print(l)


if __name__ == "__main__":
    # 类似文件操作的open
    with Manager() as manager:
        # 生成一个字典，数据内容在进程间共享
        d = manager.dict()
        # 生成一个列表，数据内容在进程间共享
        l = manager.list()

        p_list = []

        for i in range(5):
            p = multiprocessing.Process(target=run, args=(d, l))
            p.start()
            p_list.append(p)

        # 等待所有子进程执行结果，不加报错
        for process in p_list:
            process.join()

        print(d)
        print(l)