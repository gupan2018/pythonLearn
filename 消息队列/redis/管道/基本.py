# -*- coding:utf-8 -*-
# __author__ = 'gupan'
# redis-py默认在每次创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果
# 想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且
# 默认情况下一次pipline是原子性操作

import time
import redis
pool = redis.ConnectionPool(host='192.168.17.136', port=6379, db=1, password='123456')
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

pipe.set("name3", 'zhangxiaobao')
time.sleep(60)
pipe.set('role3', 'sb')
# print(pipe.get("name"))
pipe.execute()