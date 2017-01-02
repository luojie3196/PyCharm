#!/usr/bin/python
# encoding:utf-8


class Foo(object):
    def __init__(self):
        self.name = 'wupeiqi'

    def func(self, *args):
        return 'func',args


obj = Foo()

# #### 检查是否含有成员 ####
print(hasattr(obj, 'name'))
print(hasattr(obj, 'func'))

# #### 获取成员 ####
print(getattr(obj, 'name'))
func = getattr(obj, 'func')
print(func('test', 'ddddddd'))

# #### 设置成员 ####
setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)
print(getattr(obj, 'age'))
show = getattr(obj, 'show')
print(show(1))


# #### 删除成员 ####
delattr(obj, 'name')
# delattr(obj, 'func')