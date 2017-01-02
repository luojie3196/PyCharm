#!/usr/bin/python
# encoding:utf-8

list_1 = [1, 3, 4 ,5 ,6, 4, 7]
# set直接去重
list_1 = set(list_1)
# 定义集合
list_2 = set([2, 4, 6, 8, 12, 18])
print(list_1, type(list_1), list_2)

# 交集
print('交集：', list_1.intersection(list_2))

# 并集
print('并集：', list_1.union(list_2))

# 差集
print(list_1.difference(list_2))
print(list_2.difference(list_1))

# 子集
list_3 = set([1, 3, 5])
print(list_1.issubset(list_2))
print(list_1.issuperset(list_2))
print(list_1.issuperset(list_3))

# 对称差集
print(list_1.symmetric_difference(list_2))

# Return True if two sets have a null intersection.
print(list_2.isdisjoint(list_3))

# 运算符方法
# 交集
print(list_1 & list_2)
# union
print(list_2 | list_1)
# deference
print(list_1 - list_2) # in list1 not in list2
print(list_2 - list_1) # in list2 not in list1
# 对称差集
print(list_1 ^ list_2)

# 操作
list_1.add(999)
print(list_1)

list_1.update([888, 777, 555])
print(list_1)

# print(list_1.pop())
# print(list_1.pop())
# print(list_1.pop())

# print(list_1.remove('789'))
list_1.discard(7)
print(list_1)




