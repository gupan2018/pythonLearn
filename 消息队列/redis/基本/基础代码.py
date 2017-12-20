# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import redis
r = redis.Redis(host='localhost', port=6379)
r.set('name', 'yuangungun')
print(r.get('name'))