# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import socket

client = socket.socket()

client.connect(("192.168.17.133", 8888))

while True:
    str = input(">>>")
    client.send(str.encode("utf-8"))
    data = client.recv(1024)
    print(data.decode())