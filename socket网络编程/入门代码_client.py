# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import socket

# 声明socket类型，同时生成socket链接对象
client = socket.socket()
client.connect(("192.168.17.136", 8888))

# python3中只能发送byte类型数据
# client.send(b"hello world")
msg = input("请输入数据").strip()
client.send(msg.encode("utf-8"))
data = client.recv(1024)

print("recv", data.decode())
client.close()
