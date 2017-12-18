# -*- coding:utf-8 -*-
# __author__ = 'gupan'
data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}

list = []
level = 1
choice = None
while True:
    if level == 1:
        print("\033[31;1m您当前所处目录为\\\033[0m")
        print("当前目录下的子目录有：")
        for i in data:
            print(i)

    if level == 2:
        print("\033[31;1m您当前所处目录为\\" + list[0] + "\\\033[0m")
        print("当前目录下的子目录有：")
        for i in data[list[0]]:
            print(i)

    if level == 3:
        print("\033[31;1m您当前所处目录为\\" + list[0] + "\\" + list[1] + "\\\033[0m")
        print("当前目录下的子目录有：")
        for i in data[list[0]][list[1]]:
            print(i)

    if level == 4:
        print("\033[31;1m您当前所处目录为\\" + list[0] + "\\" + list[1] + "\\" + "list[2]" + "\\\033[0m")
        print("已到底层目录，输入..返回上一层目录")

    choice = input("\033[31;1m请输入想要进入的菜单>>>\033[0m")

    if choice == ".." and level > 1:
        level -= 1
        list.pop()
    if choice == "q":
        print("bye".center(50, "-"))
        break

    if level == 1:
        if (choice in data) == False:
            continue
        for i in data[choice]:
            print(i)
        level += 1
        list.append(choice)

    if level == 2:
        if data[list[0]] == {}:
            continue

        if (choice in data[list[0]]) == False:
            continue
        for i in data[list[0]]:
            print(i)
        level += 1
        list.append(choice)

    if level == 3:
        if data[list[0]][list[1]] == {}:
            continue

        if (choice in data[list[0]][list[1]]) == False:
            continue
        for i in data[list[0]][list[1]]:
            print(i)
        level += 1
        list.append(choice)