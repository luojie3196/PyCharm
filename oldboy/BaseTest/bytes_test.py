#!/usr/bin/python
# encoding:utf-8

from __future__ import division

# py3
name = '罗杰'
# convert str to bytes
b1 = bytes(name, encoding = 'utf-8')
print(b1)
b2 = bytes(name, encoding='gbk')
print(b2)
# convert bytes to str
s1 = str(b1, encoding='utf-8')
print(s1)
s2 = str(b2, encoding='gbk')
print(s2)