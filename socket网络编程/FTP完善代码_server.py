# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import socket
import hashlib
import os

server = socket.socket()
server.bind(("0.0.0.0", 8888))
server.listen(5)

'''
conn：连接的客户端连接对象
addr：连接的客户端地址
judge：从服务端发送的命令，是获取文件还是执行命令
    获取文件：以get开头

获取文件：
    get_req_addr：想要获取的文件的路径
    file_size：想要获取的文件的大小
    sha_handle：文件加密后的sha256对象
执行命令：
    cmd：需要执行的命令
    cmd_res：命令执行后的返回结果
    cmd_res_size：返回结果的长度
    client_ack：无意义，避免粘包操作
'''

while True:
    conn, addr = server.accept()
    print("recv from：", addr)
    while True:
        judge = conn.recv(1024)
        print("cmd:{cmd} address begin...".format(cmd=judge.decode()))
        if judge.decode().startswith("get"):
            get_req_addr = judge.decode()
            req_addr = get_req_addr[4:len(get_req_addr)]
            if not os.path.isfile(req_addr):
                conn.send("not this file!!!!!!{error_path}".format(
                    error_path=req_addr).encode("utf-8"))
                continue

            file_size = os.stat(req_addr).st_size
            conn.send(str(file_size).encode("utf-8"))
            conn.recv(1024)

            sha_handle = hashlib.sha256()
            with open(req_addr, "rb") as req_file:
                for line in req_file:
                    conn.send(line)
                    sha_handle.update(line)
                print("file: {file_name} send done".format(
                    file_name=req_addr
                ))

            # 发送该文件的md5值
            conn.send(sha_handle.hexdigest().encode("utf-8"))

        else:
            cmd = judge
            print(cmd.decode())
            if not cmd:
                break
            cmd_res = os.popen(cmd.decode()).read()
            # print(cmd_res)
            if not cmd_res:
                conn.send("no this conmand".encode("utf-8"))
                continue

            # 此时cmd_res是一个str类型，而encode("utf-8")之后，数据大小会变化，所以对于str类型数据，需要encode一下之后才能进行判断数据大小
            cmd_res_size = len(cmd_res.encode("utf-8"))
            conn.send(str(cmd_res_size).encode("utf-8"))
            # 采用recv后，阻塞，必须等到客户端响应之后才能执行下面的命令
            client_ack = conn.recv(1024)
            conn.send(cmd_res.encode("utf-8"))
        print("cmd:{cmd} address end".format(cmd=judge.decode()))