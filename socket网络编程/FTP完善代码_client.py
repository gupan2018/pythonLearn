# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import socket
import hashlib
import os

addr = ""
port = ""

# 输入服务器ip地址
while True:
    addr = input("Input IP addr>>>").strip()
    if "." not in addr:
        continue
    check_codes = addr.split(".")

    if len(check_codes) != 4:
        continue

    for check_code in check_codes:
        if not check_code.isdigit():
            continue
    break

# 输入端口号
while True:
    port = input("Input Port>>>").strip()
    if port.isdigit():
        port = int(port)
        break
    continue

client = socket.socket()
client.connect((addr, port))


# 客户端执行代码语句
'''
cmd：客户端输入需要服务器执行的命令
cmd_res_size：服务器执行结果长度，若执行失败，返回失败信息
recv_len：已接收的数据长度
get 从服务端拉取请求
    req_path：需要从服务端下载的文件在服务端的路径
    save_path：下载完成后的文件的保存路径
    choice：需保存路径有文件存在时是否覆盖
    sha_handle：下载后的文件的sha256码

通用参数
recv_size_once：一次下载所接受的最大字节数


'''
while True:
    cmd = input(">>>")
    if not cmd:
        continue

    if cmd == "exit":
        break

    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)

    # 执行成功，返回执行结果长度，是数字
    if not cmd_res_size.decode().isdigit():
        print(cmd_res_size.decode())
        continue

    # 若发送的命令有执行结果，那么就发送乐易ack消息，告诉server端可以发包了
    client.send("ack".encode("utf-8"))
    print("cmd_res_size:", cmd_res_size.decode())
    cmd_res_size = int(cmd_res_size.decode())
    recv_len = 0

    # 从服务端拉取文件
    if cmd.startswith("get"):
        req_path = cmd[4:len(cmd)]
        save_path = os.path.dirname(os.path.abspath(__file__)) + "/" + os.path.basename(req_path)
        print(save_path)
        choice = ""
        while True:
            if os.path.exists(save_path):
                choice = input("file exists, convert it y/n>>>").strip()
                if choice not in ["y", "n"]:
                    continue
                break
            break

        if choice == "n":
            print("get file {req_path} cancel".format(req_path=req_path))
            break

        with open(save_path, "wb") as save_file:
            sha_handle = hashlib.sha256()
            recv_size_once = 1024
            while recv_len < cmd_res_size:
                if cmd_res_size - recv_len <= 1024:
                    recv_size_once = cmd_res_size - recv_len
                recv_data = client.recv(recv_size_once)
                recv_len += len(recv_data)
                print("recv_len:{recv_len}, total_len:{total_len}".format(
                    recv_len=recv_len,
                    total_len=cmd_res_size
                ))
                sha_handle.update(recv_data)
                save_file.write(recv_data)

        sha_recv = client.recv(1024)
        if sha_handle.hexdigest() == sha_recv.decode():
            print("recv done")
        else:
            print("\033[31;1mrecv failed\033[0m")
            if os.path.exists(save_path):
                os.remove(save_path)

    # 执行操作系统命令
    else:
        cmd_res = ""
        while recv_len < cmd_res_size:
            recv_size_once = 1024
            if cmd_res_size - recv_len <= 1024:
                recv_size_once = cmd_res_size - recv_len
            recv_data = client.recv(recv_size_once)
            cmd_res += recv_data.decode()
            recv_len += len(recv_data)

        print(cmd_res)