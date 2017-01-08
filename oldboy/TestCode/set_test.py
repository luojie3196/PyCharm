#!/usr/bin/env python
# -*- coding:utf-8 -*-


list_1 = ['1', '2', '3', '4', '2', '4', '5', '6']
list_1 = set(list_1)
# print(list_1, type(list_1))

list_2 = set(('1','2','88','99','77','66','55','44','33'))
print('list_1: ', list_1)
print('list_2: ', list_2)
# print(list_2)

# 并集
# print(list_1.union(list_2))
# list_1.add('2222')
# print(list_1)
# list_1.remove('2222')
# print(list_1)

# 清空set
# list_1.clear()
# print(list_1)

# 差集
# print(list_1.difference(list_2))
# print(list_2.difference(list_1))

# 并集
# print(list_1.intersection(list_2))

list_3 = set(('1', '2', '6', '88'))
print('list_3: ', list_3)

# 子集或者父集
# print(list_1.issubset(list_3))
# print(list_3.issubset(list_1))
# print(list_1.issuperset(list_3))
# print(list_3.issuperset(list_1))

# 随机删除一个
# list_1.pop()
# print(list_1)

# print(list_1.union(list_2))

# 对称差集
# print(list_1.symmetric_difference(list_2))

# 把list_3更新到list_1中
list_1.update(list_3)
print(list_1)