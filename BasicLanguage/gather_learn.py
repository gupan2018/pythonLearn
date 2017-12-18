# -*- coding:utf-8 -*-
# __author__ = 'gupan'
set_1 = set([1, 2, 3, 4, 5, 6, 7, 8])
set_2 = set([2, 3, 4, 5, 6, 8, 9, 10])
sub_1 = {1, 2, 3}
sub_2 = {11}
print(set_1)
print(set_2)

print(set_1.intersection(set_2))
print(set_1.union(set_2))
print(set_1.difference(set_2))
print(set_2.difference(set_1))
print(sub_1.issubset(set_1))
print(sub_2.issubset(set_1))
print(set_1.issuperset(sub_1))
print(set_1.issuperset(sub_2))

print(set_1.symmetric_difference(set_2))

print(set_1.isdisjoint(set_2))
print(sub_1.isdisjoint(sub_2))

print(set_1&set_2)
print(set_1-set_2)
print(set_1|set_2)
print(set_1^set_2)

set_1.add(100)
print(set_1)

set_1.update({11, 14, 15})
print(set_1)

set_1.remove(100)
print(set_1)

set_1.pop()
print(set_1)

set_1.discard(100)
print(set_1)
set_1.discard(100)
print(set_1)

print(len(set_1))

print(2 in set_1)