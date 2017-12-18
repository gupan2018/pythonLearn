# -*- coding:utf-8 -*-
# __author__ = 'gupan'

# gevent不知道urlib是进行了IO操作，所以整个程序执行起来表现是串行的
# 那么如何让gevent知道urlib进行了IO操作呢？
# 只需要from gevent import monkey
# 在程序的开头输入monkey.patch_all()即可

from gevent import monkey

# monkey.patch_all()
import gevent
from  urllib.request import urlopen
import time

def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

urls = [ 'https://www.python.org/',
         'https://www.yahoo.com/',
         'https://github.com/'
         ]

# time_start = time.time()
# for url in urls:
#     f(url)
# print("同步cost",time.time() - time_start)

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print("异步cost",time.time()-async_time_start )