# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import select
import socket
import queue
import time

def select_server(HOST, PORT):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind( (HOST, PORT))
    server.listen(1000)
    # 设置成非阻塞
    server.setblocking(False)
    # 设置端口可重用
    # SOL_SOCKET（套接字描述符）、SO_REUSEADDR（端口复用）
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return server


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8888
    server = select_server(HOST, PORT)
    inputs = [server]
    outputs = []
    msg_dic = {}

    while True:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        for read_socket in readable:
            if read_socket is server:
                conn, addr = server.accept()
                inputs.append(conn)
                conn.setblocking(False)
                msg_dic[conn] = queue.Queue()
                # print(outputs)
                continue
            data = read_socket.recv(1024)
            msg_dic[read_socket].put(data)
            outputs.append(read_socket)
            print("recv data", data)
            if not data:
                inputs.remove(read_socket)
                outputs.remove(read_socket)
                del msg_dic[read_socket]
                read_socket.close()

        for write_socket in writable:
            try:
                data = msg_dic[write_socket].get_nowait()
                write_socket.send(data)

            except queue.Empty as e:
                print(e)
            # 确保下次循环的时候writeable,不返回这个已经处理完的连接了
            outputs.remove(write_socket)


        for except_socket in exceptional:
            print("exceptional:", exceptional)
            if except_socket in outputs:
                outputs.remove(except_socket)
            inputs.remove(except_socket)
            del msg_dic[except_socket]
            except_socket.close()