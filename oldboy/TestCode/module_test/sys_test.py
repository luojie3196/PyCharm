#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import time

# print(sys.argv)
# print(sys.path)
# print(sys.version)
# print(sys.platform)
# sys.exit(0)

def progress_bar():
    for n in range(10):
        sys.stdout.write('#')
        sys.stdout.flush()
        time.sleep(1)


val = sys.stdin.readline() # [:-1]
print(val)


