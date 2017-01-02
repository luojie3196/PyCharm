#!/usr/bin/python
# encoding:utf-8

li = ["手机", "电脑", '鼠标垫', '游艇']
for k, v in enumerate(li, 1):
    print(k, v)

inp = input('Please choose: ')
inp = int(inp)
if 0 < inp <= len(li):
    print(li[int(inp) - 1])
else:
    print('goods not exist.')