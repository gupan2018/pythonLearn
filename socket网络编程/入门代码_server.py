# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import socket
server = socket.socket()

# 绑定要监听的端口
server.bind(("localhost", 6969))

# 设置监听，设置最多可有多少个在排队，最大连接数为n + 1
server.listen(10)

# 等待客户端数据接入
# accept返回
#   客户端实例(conn)
#   地址(addr)
conn, addr = server.accept()

# 指定接受客户端的数据的最大大小
data = conn.recv(1024)
# data = data.decode()
print("recv:", data.decode())

conn.send("我已经收到了你的数据".encode("utf-8"))

server.close()