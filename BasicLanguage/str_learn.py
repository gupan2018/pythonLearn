# -*- coding:utf-8 -*-
# __author__ = 'gupan'
name = "gupan"
str = "my name is {name}, I'm {age} years old"
print(name.center(50, "-"))
print(name.endswith("an"))
#print(name.expandtabs(tabsize=30))
print(name.find("u"))
#print(str.format(name = "gupan", age = 12))
print(str.format_map({"name":"gupan", "age":12}))
print("9.22".isdigit())
print('+'.join(['1', '2', '3']))
print(name.ljust(100, "+"))
print("\ntets\n".strip())
print("----")

p = str.maketrans("gupan", "12345")
print("gupau".translate(p))

print("gupangupan".replace('g','G', 1))

str01 = "1,2,3,4,5,6"
print(str01.split(","))