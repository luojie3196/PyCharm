#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os

print(__file__)

# file_name = os.path.basename(os.path.abspath(__file__))
# pth = os.path.dirname(os.path.abspath(__file__))
# farther_path = os.path.dirname(pth)
# print(file_name)
# print(pth)
# print(farther_path)
#
# print(os.curdir, os.pardir, os.sep, os.name, os.linesep)
# print(os.listdir())
# print(os.walk('.'))
# print(os.stat('default.xml'))
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# print(os.environ['HOME'])
# print(os.getlogin())
# print(os.times())
# print(os.times_result)
# print(os.cpu_count())
print(os.path.split(os.getcwd()))
print(os.path.getatime('6.py'))
print(os.path.getmtime('6.py'))
print(os.path.isdir('.'))
print(os.path.isfile('6.py'))
print(os.path.isabs(r'D:\\'))
print(os.path.exists(r'G:\\'))
print(os.path.join('D:\\', '6.py'))