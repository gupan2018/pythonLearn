# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import socket

HOST = '192.168.17.133'  # The remote host
PORT = 8888  # The same port as used by the server

msg = "this is a message"

socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(100)]

for sock in socks:
    sock.connect((HOST, PORT))

for sock in socks:
    sock.send(msg.encode("utf-8"))

for sock in socks:
    data = sock.recv(1024)
    print(data.decode())
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# while True:
#     msg = bytes(input(">>:"), encoding="utf8")
#     s.sendall(msg)
#     data = s.recv(1024)
#
#     #
#     print('Received', data)
