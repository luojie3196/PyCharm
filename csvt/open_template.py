#!/usr/bin/python
# encoding:utf-8

filename = raw_input("Please input file: ")

try:
    f1 = open(filename)
    print hello
except IOError, msg:
    print 'This file not exist'
except NameError, msg:
    print 'Can not find hello'
finally:
    # if f1:
    #     f1.close()
    # print 'exec finally'
    try:
        f1.close()
    except NameError, msg:
        pass