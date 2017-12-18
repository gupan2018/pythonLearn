# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import time
import threading

def light():
    global count
    event.set()
    while True:
        if count >= 0 and count <= 5:
            print("red light ,please wait")
            time.sleep(1)
        elif count > 10:
            # 设置红灯
            event.set()
            count = 0
        else:
            # 判断是否设置了标志位
            if event.isSet():
                # 清空标志位，设置为绿灯，通行
                event.clear()
            print("is running")
            time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.isSet():
            print("lightor is red, waiting....")
            time.sleep(1)

        else:
            print("lightor is green, running......")
            # 等待标志位被设置
            event.wait()

count = 0
event = threading.Event()

lightor = threading.Thread(target=light, args=())
car1 = threading.Thread(target=car, args=("Tesla", ))
lightor.start()
car1.start()