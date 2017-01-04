#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import sys

def consumer(n):
    # print(n, ' Eat baozi')
    while True:
        n = yield
        # print(name, ' eat ', baozi )
        sys.stdout.write('\r' + '-'*n + '> ' + str(n) + '%')
        sys.stdout.flush()


def productor(name):
    c1 = consumer('A')
    c1.__next__()
    print('Begin eat baozi')
    for i in range(100):
        time.sleep(0.5)
        # print(name, ' make a baozi, separate to both')
        c1.send(i)


productor('alex')