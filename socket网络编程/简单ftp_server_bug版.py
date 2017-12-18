# -*- coding:utf-8 -*-
# __author__ = 'gupan'

# 代码有问题

# 注意：对于这种数据的传输，对于linux系统而言，每次只能传输缓冲区的长度，对于没有被传输的数据进行排队等候，缓冲区的数据发送后，再进行下一次发送

import socket

server = socket.socket()

server.bind(("localhost", 6969))

server.listen(5)

f_op = open("recv.avi", "wb")

while True:
    conn, addr = server.accept()
    count = 0
    while True:
        count += 1
        data = conn.recv(1024)
        f_op.write(data)
        f_op.flush()
        print("接受该数据次数%s：接受数据长度>>>" % count, len(data))
        if not data:
            f_op.close()
            break
        conn.send("from:server{count}：我已经收到你的数据>>>\n".format(count=count).encode("utf-8"))
server.close()