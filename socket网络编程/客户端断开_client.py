# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import socket
import time

client = socket.socket()
client.connect(("localhost", 6969))

while True:
    msg = input(">>>").strip()
    if msg == "b":
        break

    # 不能发送空，如果send空，程序会卡住
    if not msg:
        continue
    client.send(msg.encode(encoding="utf-8"))
    data = client.recv(1024)
    print("recv data:---------------------------------------------------------\n", data.decode())
    try:
        i = 0
        while True:
            i += 1
            print(i)
            time.sleep(0.3)
            client.send(b"a")
            client.recv(1024)
    except KeyboardInterrupt as e:
        print(e)

client.close()