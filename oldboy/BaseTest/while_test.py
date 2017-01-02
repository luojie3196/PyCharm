#!/usr/bin/python
# encoding:utf-8

# for n in range(1, 101):
#     if n % 2 != 0:
#         print(n)
#
# n =1
# while n <= 100:
#     if n % 2 == 0:
#         print(n)
#     n += 1

# odd_list = []
# even_list = []
# for n in xrange(1, 101):
#     if n % 2 != 0:
#         odd_list.append(n)
#     else:
#         even_list.append(n)
# print(odd_list)
# print(even_list)
#
# sum = 0
# for x in range(1, 100):
#     if x % 2 != 0:
#         sum += x
#     else:
#         sum -= x
# print(sum)

# n = 1
# while True:
#     if n == 4:
#         break
#     x = input('Please input: ')
#     n += 1

n = 1
s = ''
sum = 0
while n < 100:
    if n % 2 == 1:
        if n == 1:
            s = '1'
        else:
            s = s + ' + ' + str(n)
        sum += n
    else:
        s = s + ' - ' + str(n)
        sum -= n
    n += 1
print(s)
print(sum)











