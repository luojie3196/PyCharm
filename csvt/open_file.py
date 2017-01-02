#!/usr/bin/python
# encoding:utf-8

import re

f1 = open('test.txt', 'a+')
new_list = []
for line in f1.readlines():
    new = line.replace('hello', 'csvt')
    new_list.append(new)
f1.close()
f1 = open('test.txt', 'w')
f1.writelines(new_list)
f1.close()