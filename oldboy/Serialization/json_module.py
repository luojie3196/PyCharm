#!/usr/bin/python
# encoding:utf-8

import json

info = {
    'name':'alex',
    'age':'28'
}

f = open('test.text', 'w')
f.write(json.dumps(info))
f.close()

f = open('test.text', 'r')
data = json.loads(f.read())
f.close()
print(data['name'])