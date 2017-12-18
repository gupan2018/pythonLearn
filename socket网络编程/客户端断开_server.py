# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import os
import socket

server = socket.socket()
server.bind(("localhost", 6969))

# 设置监听，设置最多可有多少个在排队，最大连接数为n + 1
server.listen(2)

while True:
    # 这一句一定要放在循环体外面，放在里面原来的连接没有断开
    conn, addr = server.accept()

    # 注意，linux和windows表现不一样，linux会无限循环（接收数据为空），windows直接出错

    count = 0
    while True:

        count += 1
        print("尝试连接次数：", count)
        data = conn.recv(1024)
        # recv()中的值最多不应多余8192

        if not data:
            print("客户端断开")
            break
        res = os.popen(data.decode()).read()
        print("recv:data:-------------------\n%s\n-----------------------end---------------------------" % data.decode())
        print("send:data:-------------------\n%s\n-----------------------end---------------------------" % res)
        print(type(res))

        # 避免执行结果为空，发送空数据
        if not res:
            conn.send("执行结果为空".encode("utf-8"))
            # 执行ipconfig时，1024的大小发不完执行结果，会把这些结果放在
            # 缓冲区中，下一次有消息发过来，他会先将执行结果放在缓冲区，按
            # 队列先后发送缓冲区中的数据
            # 注意：客户端并不是每次都收1024
            continue
        conn.send(res.encode("utf-8"))
        # send这个函数并不是我们一调用的时候就发送数据，是先把数据存到缓冲区，
        # 缓冲区满了系统调用接口自动发送
        # 另一种情况：在我们手动调用send函数的时候，相当于强制超时，此时服务端
        # 不在等缓冲区的数据满了之后再发送，而是直接发送数据
        '''
            即服务器给客户端（客户端给服务器）发送数据有两种情况：
            /**
            * 1. 缓冲区满了
            * 2. 手动调用send函数，强制超时后进行数据发送
            **/
        '''
        # conn.sendall(res)

server.close()

# res = os.popen("dir").read()
#
# print(type(res))
# print(res)