# -*- coding:utf-8 -*-
# __author__ = 'gupan'

# class Father:
#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2
#
# class Child(Father):
#     def __init__(self, p1, p2, p3):
#         Father.__init__(self, p1, p2)
#         self.p3 = p3

class Father:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Child(Father):
    def __init__(self, p1, p2, p3):
        super(Child, self).__init__(p1, p2)
        self.p3 = p3

C = Child("name", "age", "money")
print(C.p1, C.p2, C.p3)

# class Father:
#     def __init__(self):
#         pass
#     def say(self):
#         print("Father say yes")
#
# class Child(Father):
#     def say(self):
#         Father.say(self)
#         print("Child say yes")
#
# C = Child()
# C.say()