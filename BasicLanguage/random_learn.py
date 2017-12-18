# -*- coding:utf-8 -*-
# __author__ = 'gupan'

import random

checkcode=""

for i in range(4):
    Flag = random.randint(0, 1)
    current = 0
    if Flag == 0:
        current = random.randint(0, 9)
    else:
        current = random.randint(65, 90) #65到90是大写字母A-Z的ascll码
        current = chr(current)
    checkcode += str(current)

print(checkcode)

