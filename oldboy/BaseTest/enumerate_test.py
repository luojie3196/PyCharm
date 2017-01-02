#!/usr/bin/python
# encoding:utf-8

lst = ['Computer', 'Cellphone', 'Mouse', 'Keyboard']
for key, item in enumerate(lst, 1):
    print(key, item)
choice = input('Please input your choice: ')
print(lst[int(choice) - 1])