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


def operator(x, o, y):
    if o == '+':
        print jia(x, y)
    elif o == '-':
        print jian(x, y)
    elif o == '*':
        print cheng(x, y)
    elif o == '/':
        print chu(x, y)
    else:
        pass

operator(1, '+', 4)