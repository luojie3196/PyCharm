#!/usr/bin/python
# -*- coding:utf-8 -*-

import random



def random_code(num):
    n = 0
    code = ''
    while n <= num:
        if n != random.randint(0, num):
            code += chr(random.randint(65, 90))
        else:
            code += str(random.randint(0, 9))
        n += 1
    return code

print(random_code(10))

# checkcode = ''
# for i in range(4):
#     current = random.randrange(0,4)
#     if current != i:
#         temp = chr(random.randint(65,90))
#     else:
#         temp = random.randint(0,9)
#     checkcode += str(temp)
# print (checkcode)