#!/usr/bin/python
# encoding:utf-8

# yield 已经把函数变成生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

f = fib(10)
print(f)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

while True:
    try:
        # x = f.__next__()
        x = next(f)
        print(x)
    except StopIteration as e:
        print('Generator return value: ', e.value)
        break

print('--------- start loop ------------')
for i in f:
    print(i)