#!/usr/bin/python
# encoding:utf-8

from __future__ import division


def jia(x, y):
    return x + y


def jian(x, y):
    return x - y


def cheng(x, y):
    return x * y


def chu(x, y):
    return x / y

operator = {'+':jia, '-':jian, '*':cheng, '/':chu}
print (operator.get('+')(1, 3))


def f(x, o, y):
    print (operator.get(o)(x, y))

f(1, "+", 2)

# print(__main__)
