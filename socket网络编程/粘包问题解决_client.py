# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import socket

client = socket.socket()

client.connect(("192.168.17.133", 8888))

while True:
    cmd = input(">>>")
    if not cmd:
        continue

    if cmd == "exit":
        break

    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)

    if cmd_res_size.decode() == "no this conmand":
        print("no this conmand")
        continue

    # 若发送的命令有执行结果，那么就发送乐易ack消息，告诉server端可以发包了
    client.send("ack".encode("utf-8"))
    print("cmd_res_size:", cmd_res_size.decode())
    cmd_res_size = int(cmd_res_size.decode())

    recv_len = 0

    cmd_res = ""

    while recv_len != cmd_res_size:
        recv_data = client.recv(1024)
        recv_len += len(recv_data)
        cmd_res += recv_data.decode()

    print(cmd_res)