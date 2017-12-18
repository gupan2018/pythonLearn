# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import hmac

m = hmac.new(b"gupan", "天王盖地虎".encode(encoding="utf-8"))
print(m.hexdigest())