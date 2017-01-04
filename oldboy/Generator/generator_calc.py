#!/usr/bin/python
# encoding:utf-8


import time


def consumer(name):
    print(name, ' Eat baozi')
    while True:
        baozi = yield
        print(name, ' eat ', baozi )


def productor(name):
    c1 = consumer('A')
    c2 = consumer('B')
    c1.__next__()
    c2.__next__()
    print('Begin eat baozi')
    for i in range(10):
        time.sleep(1)
        print(name, ' make a baozi, separate to both')
        c1.send(i)
        c2.send(i)

productor('alex')
