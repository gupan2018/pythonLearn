# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import redis
pool = redis.ConnectionPool(host='192.168.17.136', port=6379, db=1, password='123456')
r = redis.Redis(connection_pool=pool)
r.set('age', 12)
print(r.get('age'))