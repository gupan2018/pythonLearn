# -*- coding:utf-8 -*-
# __author__ = 'gupan'
'''dic = dict.fromkeys(["stu_names", "teacher_names", "other_names"], ["gupan", {"stb":"Gupan"}, "huangli"])
print(dic)
dic["stu_names"][1]["stb"] = "yuang"
print(dic)'''
dic_1 = {"stu_1":"gupan", "stu_2":"huanli", "stu_3":"gongjinjin"}
dic_1.setdefault("stu_1", "lizheng")
dic_1.setdefault("stu_4", "xiaobao")
print(dic_1.items())