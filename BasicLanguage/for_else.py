# -*- coding:utf-8 -*-
# __author__ = 'gupan'
match_num = 100
count = 0
while count < 3:
    num = int(input("请输入猜测的值："))
    if num < match_num:
        print("smaller")
    elif num > match_num:
        print("bigger")
    else:
        print("equal")
        break
    count += 1
    if count == 3:
        continue_confirm = input("do you want to continue guess?")
        if continue_confirm != 'n':
            count = 0
else:
    print("error")

