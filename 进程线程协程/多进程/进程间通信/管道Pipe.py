# -*- coding:utf-8 -*-
# __author__ = 'gupan'

from multiprocessing import Process, Pipe


def child(conn):
    conn.send([42, None, "hello"])
    print("from parent:", conn.recv())


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=child, args=(child_conn, ))
    p.start()
    print("from child:", parent_conn.recv())
    # parent_conn.send([42, None, "一切可好"])
    parent_conn.send("一切可好")