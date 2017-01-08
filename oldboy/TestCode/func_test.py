#!/usr/bin/env python
# -*- coding:utf-8 -*-

def test(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)


test(1, 2, 3, 4, 5, 6, 7, 8, ('a', 'b', 'c'), *[11,22,33,44],  a = '1', b = '2', **{'name':'luojie', 'age':28, 'sex':'male'})
test(1, 2, 3, 4, 5, 6, 7, 8, ('a', 'b', 'c'), a = '1', b = '2', *[11,22,33,44], **{'name':'luojie', 'age':28, 'sex':'male'})

def test1(x, y):
    print(x + y)

t = (11, 12)
test1(*t)