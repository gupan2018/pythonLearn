# -*- coding:utf-8 -*-
# __author__ = 'gupan'

# 当发送数据多于指定接受数据时，发送端会将数据放在缓冲区中，在接受端
# 再一次调用recv函数时进行发送
# 若不做处理，会出现下一次执行接收端发送请求，发送端发送的还是上一次
# 没有发送完的结果的情况

'''
bug解决办法
/**
* 1. 发送端在发送数据时，先告诉接受端自己数据的大小，之后再发送数据
* 2. 接受端得到发送端的数据大小信息后进行解析，之后再确定本次接受调用
    recv函数的次数
**/
'''

import os
import socket

server = socket.socket()
server.bind(("0.0.0.0", 8888))
server.listen(5)

while True:
    conn, addr = server.accept()
    print("recv from :", addr)

    while True:
        cmd = conn.recv(1024)
        if not cmd:
            break
        cmd_res = os.popen(cmd.decode()).read()
        print(cmd_res)
        if not cmd_res:
            conn.send("no this conmand".encode("utf-8"))
            continue

        # 此时cmd_res是一个str类型，而encode("utf-8")之后，数据大小会变化，所以对于str类型数据，需要encode一下之后才能进行判断数据大小
        cmd_res_size = len(cmd_res.encode("utf-8"))
        conn.send(str(cmd_res_size).encode("utf-8"))
        # 采用recv后，阻塞，必须等到客户端响应之后才能执行下面的命令
        client_ack = conn.recv(1024)
        conn.send(cmd_res.encode("utf-8"))