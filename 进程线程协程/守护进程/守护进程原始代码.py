# -*- coding:utf-8 -*-
# __author__ = 'gupan'

'''
守护进程编写步骤：
    1. fork子进程，而后父进程退出，此时子进程会被init进程接管。
    2. 修改子进程的工作目录chdir、创建新进程组和新会话setsid、修改umask。
        子进程在创建的时候会继承父进程的工作目录，如果执行的程序是在u盘里的，就会导致u盘不能卸载。
    3. 子进程再次fork一个进程，这个进程可以称为孙子进程，而后子进程退出。
    4. 重定向孙子进程的标准输入流、标准输出流、标准错误流到/dev/null。
'''

import os
import sys
import atexit


def daemonize(pid_file=None):
    """
    创建守护进程
    :param pid_file: 保存进程id的文件
    :return:
    """
    # 从父进程fork一个子进程出来
    pid = os.fork()
    # 子进程的pid一定为0，父进程大于0
    if pid:
        # 退出父进程，sys.exit()方法比os._exit()方法会多执行一些刷新缓冲工作
        sys.exit(0)

    # 子进程默认继承父进程的工作目录，最好是变更到根目录，否则回影响文件系统的卸载
    os.chdir('/')
    # 子进程默认继承父进程的umask（文件权限掩码），重设为0（完全控制），以免影响程序读写文件
        # 由于umask会屏蔽权限，所以设定为0，这样可以避免读写文件时碰到权限问题。
    os.umask(0)
    # 让子进程成为新的会话组长和进程组长
        # 使用setsid后，子进程就会成为新会话的首进程（session leader）；子进程会成为新进程组的组长进程；子进程没有控制终端。
    os.setsid()

    # 注意了，这里是第2次fork，也就是子进程的子进程，我们把它叫为孙子进程
        # 经过上面几个步骤后，子进程会成为新的进程组老大，可以重新申请打开终端，为了避免这个问题，fork孙子进程出来。
    _pid = os.fork()
    if _pid:
        # 退出子进程
        sys.exit(0)

    # 此时，孙子进程已经是守护进程了，接下来重定向标准输入、输出、错误的描述符(是重定向而不是关闭, 这样可以避免程序在 print 的时候出错)

    # 刷新缓冲区先，小心使得万年船
    sys.stdout.flush()
    sys.stderr.flush()

    # dup2函数原子化地关闭和复制文件描述符，重定向到/dev/nul，即丢弃所有输入输出
    with open('/dev/null') as read_null, open('/dev/null', 'w') as write_null:
        os.dup2(read_null.fileno(), sys.stdin.fileno())
        os.dup2(write_null.fileno(), sys.stdout.fileno())
        os.dup2(write_null.fileno(), sys.stderr.fileno())

    # 写入pid文件
    if pid_file:
        with open(pid_file, 'w+') as f:
            f.write(str(os.getpid()))
        # 注册退出函数，进程异常退出时移除pid文件
        atexit.register(os.remove, pid_file)