# -*- coding:utf-8 -*-
# __author__ = 'gupan'

class Dog(object):
    def __init__(self, name):
        self.name = name

    @classmethod
    def eat2(self, food):
        print("{name} is eating {food}".format(name = self.name, food = food))

dog = Dog("Jack")
dog.eat2("baozi")