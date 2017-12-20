# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import redis
pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('age', 12)
print(r.get('age'))