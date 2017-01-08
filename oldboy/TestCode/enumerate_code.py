#!/usr/bin/env python
# -*- coding:utf-8 -*-

project_list = ['alto45', 'alto5', 'idol3', 'idol4s', 'simba6x', 'idol3cn']

for key, lst in enumerate(project_list, 1):
    print(key, lst)

inp = input('Please choose project: ')

inp_num = int(inp) -1

print(project_list[inp_num])

str('123')
