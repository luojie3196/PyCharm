#!/usr/bin/python
# encoding:utf-8


list1 = ['name', 'age', 'gender']
list2 = ['Roger', '28', 'male']

ret = zip(list1, list2)
print(ret)

dict1 = dict(ret)
print(dict1)

list_k = list(dict1.keys())
list_v = list(dict1.values())
print(list_k, list_v)
