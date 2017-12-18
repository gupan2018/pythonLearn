# -*- coding:utf-8 -*-
# __author__ = 'gupan'
# 最简单的携程
import time
def consumer(name):
    print("%s准备收礼物了!" %name)
    while True:
       gift = yield

       print("礼物[%s]来了,被[%s]签收!" %(gift,name))

c = consumer("ChenRonghua")
c.__next__()

def producer(name):
    c = consumer('饼饼')
    c2 = consumer('海绵')
    print(c.__next__())
    print(c2.__next__())
    print("%s开始派送礼物了" % name)
    for i in range(10):
        time.sleep(1)
        print("准备了两个礼物,开始派送!")
        c.send(i)
        c2.send(i)

producer("滚滚")