# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import select
import socket
import queue


def epoll_server(address):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(address)
    server.listen(5)
    server.setblocking(False)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return server


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8888
    address = (HOST, PORT)
    server = epoll_server(address)
    timeout = 10

    epoll = select.epoll()
    epoll.register(server.fileno(), select.EPOLLIN)

    msg_dic = {}

    fd_to_socket = {server.fileno():server}

    while True:
        events = epoll.poll(timeout)
        if not events:
            continue

        for fd, event in events:
            socket = fd_to_socket[fd]
            if socket == server:
                print("server")
                conn, addr = socket.accept()
                conn.setblocking(False)
                epoll.register(conn.fileno(), select.EPOLLIN)
                fd_to_socket[conn.fileno()] = conn
                msg_dic[conn] = queue.Queue()

            elif event & select.EPOLLHUP:
                print("epollhup")
                epoll.unregister(fd)
                fd_to_socket[fd].close()
                del msg_dic[fd_to_socket[fd]]
                del fd_to_socket[fd]

            elif event & select.EPOLLIN:
                print("event", event)
                print("select.EPOLLIN", select.EPOLLIN)
                print("epollin")
                data = socket.recv(1024)
                if data:
                    msg_dic[socket].put(data)
                    epoll.modify(fd, select.EPOLLOUT)
                else:
                    epoll.modify(fd, select.EPOLLHUP)

            elif event & select.EPOLLOUT:
                print("epollout")
                try:
                    msg = msg_dic[socket].get_nowait()
                except queue.Empty as e:
                    print(socket.getpeername(), "queue empty")
                    epoll.modify(fd, select.EPOLLHUP)
                else:
                    print("发送数据", msg, "客户端", socket.getpeername())
                    socket.send(msg)
                    epoll.modify(fd, select.EPOLLIN)
    epoll.unregister(server, server.fileno())
    epoll.close()
    server.close()
