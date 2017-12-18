# -*- coding:utf-8 -*-
# __author__ = 'gupan'

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def eat(self):
        print("{name} is eating".format(name = self.name))

    def talk(self):
        print("{name} is talking".format(name = self.name))

    def sleep(self):
        print("{name} is sleeping".format(name = self.name))

class Relation(object):
    def __init__(self):
        pass

    def make_friend(self, obj):
        print("{self_name} is making friends with {friend_name}".format(self_name = self.name, friend_name = obj.name))
        self.friends.append(obj)


class Man(People, Relation):
    # def __init__(self, name, age):
    #     Relation.__init__(self)
    #     People.__init__(self, name, age)
    #     #super(Man, self).__init__(name, age)

    def piao(self):
        print("{name} is piaoing".format(name = self.name))

    def sleep(self):
        print("{name} is sleepig".format(name = self.name))

class Woman(People, Relation):
    def get_birth(self):
        print("{name} born a baby".format(name = self.name))

m1 = Man("gupan", 24)
w1 = Woman("huangli", 25)
m1.make_friend(w1)
print(m1.friends[0].name)
