#!/usr/bin/python
# encoding:utf-8

import pickle

def test():
    print('test')

info = {
    'name':'alex',
    'age':'28',
    'func':test
}

f = open('test.text', 'wb')
# f.write(pickle.dumps(info))
pickle.dump(info, f)
f.close()

f = open('test.text', 'rb')
# data = pickle.loads(f.read())
data = pickle.load(f)
f.close()
print(data)