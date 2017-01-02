#!/usr/bin/python
# encoding:utf-8


import shutil

# f1 = open('test.txt', encoding='utf-8')
# f2 = open('test_bak.txt', 'w', encoding='utf-8')
#
# shutil.copyfileobj(f1, f2)

shutil.copyfile('test.txt', 'test_bak1.txt')

# shutil.copymode()
# shutil.copyfile() #only copy file
# shutil.copy() #copy file and mode
# shutil.copytree() # copy dir
# shutil.rmtree() # remove dir
#shutil.move()
# shutil.make_archive(r'D:\oldboy', 'zip', r'C:\Users\Yuan Yuan\PycharmProjects\csvt\oldboy')

import zipfile

z = zipfile.ZipFile('day5.zip', 'w')
z.write('while_test.py')
print('waiting...')
z.write('enumerate_test.py')
z.close()