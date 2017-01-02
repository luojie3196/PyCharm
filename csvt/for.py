#!/usr/bin/python
# encoding:utf-8

import time
s = 'hello'
l = [1, 2, 3, 'a', 'b']
t = (7, 8, 9, 'x', 'y')
d = {1:111, 2:222, 3:333}

for x in d:
    print d[x]
    time.sleep(1)
    if x == 3:
        break
else:
    print 'ending'

print d.items()
for k, v in d.items():
    print k
    print v
a, b, c, d, e = t
print a, b, c, d, e

for x in range(len(s)):
    print s[x]

for x in s:
    print x

for x in l:
    if x > 2:
        print x
