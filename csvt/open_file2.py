#!/usr/bin/python
# encoding:utf-8

import re


f1 = open('test.txt', 'r')
txt = f1.read()
f1.close()
# print txt
lst = re.findall('hello', txt)
print 'find %d hello string' % len(lst)


