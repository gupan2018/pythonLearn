# -*- coding:utf-8 -*-
# __author__ = 'gupan'

# def func(self):
#     print("{name}这是另一种定义一个类的方法".format(name = self.name))
#
# def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# Foo = type("Foo", (object, ), {"talk":func,
#                                "__init__":__init__})
#
# f = Foo("goudan", 22)
# f.talk()

class MyType(type):
     def __init__(self,*args,**kwargs):

         print("Mytype __init__",*args,**kwargs)

     def __call__(self, *args, **kwargs):
         print("Mytype __call__", *args, **kwargs)
         obj = self.__new__(self)
         print("obj ",obj,*args, **kwargs)
         print(self)
         self.__init__(obj,*args, **kwargs)
         return obj

     def __new__(cls, *args, **kwargs):
         print("Mytype __new__",*args,**kwargs)
         return type.__new__(cls, *args, **kwargs)

print('here...')

class Foo(object,metaclass=MyType):
    def __init__(self,name):
        self.name = name

        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__",cls, *args, **kwargs)
        return object.__new__(cls)

f = Foo("Alex")
print("f",f)
print("fname",f.name)