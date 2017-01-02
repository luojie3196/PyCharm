#!/usr/bin/python
# encoding:utf-8

li = [11,22,33,44,55,66,77,88,99,90]
li1 = []
li2 = []
dic = {}
for n in li:
    print(type(n))
    if n >= 66:
        li1.append(n)
    else:
        li2.append(n)
dic['k1'] = li1
dic['k2'] = li2
print(dic)
