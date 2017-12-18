# -*- coding:utf-8 -*-
# __author__ = 'gupan'
import hashlib

m = hashlib.md5()
#有中文是不能加b，并且需要将带中文的字符串编码为utf-8格式
m.update("Hello Mr顾".encode(encoding="utf-8"))
#16进制格式hash
print("16进制格式hash", m.hexdigest())
#2进制格式hash
print("二进制格式hash", m.digest())

print("16进制，验证一致性", m.hexdigest())
m.update(b"It's me")#与前面的值进行更新

print(m.hexdigest())