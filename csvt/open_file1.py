#!/usr/bin/python
# encoding:utf-8

import re

f1 = open('test.txt', 'a+')
f2 = open('result.txt', 'a+')
new_list = []
for line in f1.readlines():
    new = line.replace('hello', 'csvt')
    new_list.append(new)
# print new_list
f2.writelines(new_list)
f1.close()
f2.close()