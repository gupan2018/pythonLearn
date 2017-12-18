# -*- coding:utf-8 -*-
# __author__ = 'gupan'

class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat(food):
        print(" is eating {food}".format(food = food))

    @staticmethod
    def eat2(self, food):
        print("{name} is eating {food}".format(name = self.name, food = food))


dog = Dog("Jack")
dog.eat2(dog, "baozi")
Dog.eat("baozi")
