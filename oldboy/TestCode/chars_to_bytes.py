#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Py3 字节和字符转换
name = '罗杰'
for n in name:
    print(n)
    byte_list = bytes(n, encoding='utf-8')
    print(byte_list)
    for b in byte_list:
        print(b, bin(b), hex(b))