# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import selectors34
import socket

def accept(server, mask):
    conn,addr = server.accept()
    print("accepted", conn, "from", addr, mask)
    conn.setblocking(False)
    sel.register(conn, selectors34.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if data:
        print("echoing", repr(data), "to", conn)
        conn.send(data)
    else:
        print("closing", conn)
        conn.close()


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8888
    sel = selectors34.DefaultSelector()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    server.setblocking(False)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sel.register(server, selectors34.EVENT_READ, accept)
    while True:
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)