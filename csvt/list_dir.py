#!/usr/bin/python
# encoding:utf-8

import os

def dirList(path):
    all_file = []
    for path, d ,fileList in os.walk(path):
        for filename in fileList:
            all_file.append(os.path.join(path, filename))
    return all_file


x = dirList('C:\\Users\\Yuan Yuan\\PycharmProjects\\csvt\\')