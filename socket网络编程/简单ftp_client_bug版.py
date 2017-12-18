# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import os
import socket

client = socket.socket()

client.connect(("localhost", 6969))

f_op = open("test01.avi", "rb")
msg = f_op.read()
while True:
    choice = input("发着玩>>>")
    if choice == "b":
        break
    client.send(msg)
    data = client.recv(1024)
    print(data.decode())

client.close()
