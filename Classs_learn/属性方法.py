# -*- coding:utf-8 -*-
# __author__ = 'gupan'

class Dog(object):
    def __init__(self, name):
        self.name = name
        self.__food = None

    @property
    def eat2(self):
        print("{name} is eating {food}".format(name = self.name, food = self.__food))

    @eat2.setter
    def eat2(self, food):
        print("{name} is eating {food}".format(name = self.name, food = food))
        self.__food = food

    @eat2.deleter
    def eat2(self):
        del self.__food
        print("删除完毕".center(50, "-"))

    def __call__(self, *args, **kwargs):
        print(self.name ,"is calling")
        pass

dog = Dog("Jack")
# dog.eat2
# dog.eat2 = "baozi"
# del dog.eat2
# # dog.eat2
# dog()

print(Dog.__dict__)
print(dog.__dict__)