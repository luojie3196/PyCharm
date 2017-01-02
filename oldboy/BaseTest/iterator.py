#!/usr/bin/python
# encoding:utf-8


for x in range(10):
    print(x)


# py3 上下完全等价
it = iter(range(10))

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration as e:
        break
