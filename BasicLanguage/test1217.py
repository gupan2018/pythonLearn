# -*- coding:utf-8 -*-
# __author__ = 'gupan'
from test import MyTest
import gevent
gevent.joinall([
        gevent.spawn(MyTest().test_1),
        gevent.spawn(MyTest().test_2)
])