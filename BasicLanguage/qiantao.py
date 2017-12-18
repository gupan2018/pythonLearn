# -*- coding:utf-8 -*-
# __author__ = 'gupan'
def grandpa():
    x = 1
    def dad():
        x =2
        def son():
            x = 3
            print(x)
        son()
    #dad()
grandpa()
