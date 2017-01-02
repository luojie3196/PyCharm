#!/usr/bin/python
# encoding:utf-8

import shelve
import datetime

d = shelve.open('shelve.txt')
print(d.get('name'))
print(d.get('info'))
print(d.get('date'))


# info = {'age':22, 'job':'it'}
#
# name = ['alex', 'rain', 'test']
# d['name'] = name
# d['info'] = info
# d['date'] = datetime.datetime.now()
# d.close()