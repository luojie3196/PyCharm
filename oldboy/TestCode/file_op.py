#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

f = open(r'D:\db_int.sql', 'r+', encoding='utf-8')

# f.readlines()
# print('tell: ', f.tell())
# f.seek(0, 0)
# print('tell: ', f.tell())
# print('fileno:', f.fileno())
# # 截取10个字符
# # print('truncate: ', f.truncate(10))
# print('writable: ', f.writable())
# print('readable: ', f.readable())
#
# f.read()
# f.seek(0, 0)
# f.readline()
# f.seek(0, 0)
# f.readlines()
# f.seek(30, 0)
# f.write('\ntest\n')
# f.writelines(['12345\n', 'abcdefg\n'])

f.close()

# with open(r'D:\db_int.sql', 'r+', encoding='utf-8') as f:
#     time_format = '%Y-%m-%d %X'
#     current_time = time.strftime(time_format)
#     print(current_time, f.read())

with open(r'D:\db_int.sql', 'r+', encoding='utf-8') as f:
    print(f)
    for line in f:
        print(line)
