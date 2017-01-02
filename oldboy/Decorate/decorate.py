#!/usr/bin/python
# encoding:utf-8

import time

def timer(func):
    def decorate(*args, **kwargs):
        start_time = time.time()
        # print(func)
        func(*args, **kwargs)
        end_time = time.time()
        print('Run time: %s' %(end_time - start_time))
    return decorate

@timer # main = timer(main)
def main(x, y):
    time.sleep(1)
    print('In the main func x + y = %d' %(x + y))

@timer
def main1():
    time.sleep(2)
    print('In the main1 func')

main(1, 8)
main1()