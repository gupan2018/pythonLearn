# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import multiprocessing
from multiprocessing import Pool
import os,time


def run_test(num):
    print("child process:", os.getppid())
    time.sleep(2)


def callback_test(args):
    print(args)
    print("回调函数中的arg参数")
    print("调用回调函数，调用进程是：", os.getpid())


if __name__ == "__main__":
    pool = Pool(processes=5)
    print("主线程PID：", os.getppid())
    for i in range(10):
        # 调用apply函数，程序串行
        # pool.apply(func=run_test, args=(i, ))

        # 调用apply_async，程序并行
        # pool.apply_async(func=run_test, args=(i, ))

        # 在pool中的所有子进程执行完毕之后，调用callback中的函数（回调函数）,注意穿参方式
        # 应用场景：在子进程结束之后对数据库进行插入操作，避免数据库连接池数目过大
        pool.apply_async(func=run_test, args=(i,), callback=callback_test)

    print("end")

    # 一定要先close()，然后再join，否则程序出错
    # 如果不join，主进程不会等子进程执行结果，执行完毕之后直接退出，子线程没有执行
    pool.close()
    pool.join()
