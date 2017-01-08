#!/usr/bin/python
# -*- coding:utf-8 -*-


# py2
temp = '罗杰' # utf-8

# 解码，需要指定原来是什么编码
temp_unicode = temp.decode('utf-8')

# 编码，需要指定要编成什么编码
temp_gbk = temp_unicode.encode('gbk')

# py3
# temp_gbk = temp.encode('gbk')