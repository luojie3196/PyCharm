#!/usr/bin/python
# -*- coding:utf-8 -*-

import hashlib


m = hashlib.md5()
m.update('luojie'.encode('utf-8'))

# print(m.digest()) #2进制格式hash
# print(m.hexdigest()) #16进制格式hash


hash = hashlib.md5()
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

# ######## sha1 ########

# hash = hashlib.sha1()
# hash.update('admin'.encode('utf-8'))
# print(hash.hexdigest())

# ######## sha256 ########

# hash = hashlib.sha256()
# hash.update('admin'.encode('utf-8'))
# print(hash.hexdigest())

# ######## sha384 ########

# hash = hashlib.sha384()
# hash.update('admin'.encode('utf-8'))
# print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())


# 它内部对我们创建 key 和 内容 再进行处理然后再加密
import hmac
h = hmac.new('wueiqi'.encode('utf-8'))
h.update('hellowo'.encode('utf-8'))
print(h.hexdigest())