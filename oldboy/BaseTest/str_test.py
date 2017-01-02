#!/usr/bin/python
# encoding:utf-8

li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

# for x in li:
# for x in tu:
for x in dic.values():
    new_str = x.strip()
    if (new_str.startswith('a') or new_str.startswith('A')) and new_str.endswith('c'):
        print(x)
    # print(new_str)