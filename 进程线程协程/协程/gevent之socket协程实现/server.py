# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import socket
import gevent

from gevent import monkey

monkey.patch_all()

def socket_handle(conn):
    try:
        while True:
            data = conn.recv(1024)
            conn.send(data.upper())
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except ConnectionResetError as e:
        print(e)
    finally:
        conn.close()


def server(port):
    server = socket.socket()
    server.bind(("localhost", port))
    server.listen(500)
    while True:
        conn, addr = server.accept()
        gevent.spawn(socket_handle, conn)


if __name__ == "__main__":
    server = server(8888)