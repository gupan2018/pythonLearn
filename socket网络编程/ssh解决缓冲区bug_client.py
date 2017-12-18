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

    print("cmd_res_size:", cmd_res_size.decode())
    cmd_res_size = int(cmd_res_size.decode())

    recv_len = 0

    cmd_res = ""

    while recv_len != cmd_res_size:
        recv_data = client.recv(1024)
        recv_len += len(recv_data)
        cmd_res += recv_data.decode()

    print(cmd_res)

    # 代码bug，每次收到的数据大小不一定是1024，所以不能用这种方式进行判断
    # add_count = 0 if 0 == cmd_res_size % 1024 else 1
    # print("add_count：", add_count)
    # recv_count = cmd_res_size // 1024 + add_count
    # print("recv_count：", recv_count)
    # res_data = ""
    # while recv_count > 0:
    #     data = client.recv(1024)
    #     res_data += data.decode()
    #     recv_count -= 1
    # print(res_data)