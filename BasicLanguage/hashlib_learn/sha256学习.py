# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import hashlib
import pickle
m = hashlib.sha256()
m.update(b"Hello")
print(m.hexdigest())
# #16进制格式hash
# print("16进制格式hash", m.hexdigest())
# #2进制格式hash
# print("二进制格式hash", m.digest())
#
# print("16进制，验证一致性", m.hexdigest())
# m.update(b"It's me")#与前面的值进行更新
#
# print(m.hexdigest())
m.update(b"World")
print(m.hexdigest())

test1 = pickle.dumps(m)

m1 = pickle.loads(test1)
if m1.hexdigest() == m.hexdigest():
    print("same")
else:
    print("not same")