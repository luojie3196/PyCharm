#!/usr/bin/python
# encoding:utf-8

print(all([1, -1, 3]))
print(any([1, -1, 3]))
print(ascii([1, 2, '罗杰']))
bin(10)
bool()
a = bytes('abcde', encoding='utf-8')
b = bytearray('abcde', encoding='utf-8')
print(a.capitalize(), a)
print(b[0], b)
print(chr(97))
ord('a')

# 可用于从远程获取代码块直接执行
code = '1+3/2*6'
c = compile(code, '', 'exec')
exec(c)
exec(code)

divmod(5, 2)
print(eval('5 + 2'))

calc = lambda n:3 if n < 4 else n
print(calc(2))

# res = filter(lambda n: n >5, range(10))
# res = map(lambda n: n*n, range(10))
# res = [lambda n:n*2 for n in range(10)]
# for i in res:
#     print(i)

# import functools
# res = functools.reduce(lambda x,y:x+y, range(10))
# print(res)

# print(globals())
# def test():
#     local_var = 333
#     print(locals())

# repr()


a = {6:1, 5:0, -1: 7}
# 按照key排序
print(sorted(a.items()))
# 按照value排序
print(sorted(a.items(), key = lambda x: x[1]))

__import__('os').system('dir')
