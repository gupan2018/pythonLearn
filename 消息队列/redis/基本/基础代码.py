# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import redis
r = redis.StrictRedis(host='192.168.17.136', port=6379, db=1, password='123456')
r.set('name', 'yuangungun')
print(r.get('name'))