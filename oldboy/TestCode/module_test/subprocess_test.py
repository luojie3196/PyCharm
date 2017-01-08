#!/usr/bin/python
# -*- coding:utf-8 -*-


import subprocess


# 执行命令，返回命令执行状态 ， 0 or 非0
# ret = subprocess.call(['ls', '-l'])
# print(ret)
# ret = subprocess.call('ls -l')
# 执行命令，如果命令结果为0，就正常返回，否则抛异常
# ret = subprocess.check_call('ls -l')
# print(ret)

# 接收字符串格式命令，返回元组形式，第1个元素是执行状态，第2个是命令结果
# ret = subprocess.getstatusoutput('ls -l')
# print(ret)

# 接收字符串格式命令，并返回结果
# ret = subprocess.getoutput('ls -l')
# print(ret)

# 执行命令，并返回结果，注意是返回结果，不是打印
# ret = subprocess.check_output('ls')
# print(ret)

#上面那些方法，底层都是封装的subprocess.Popen

# p = subprocess.Popen("df -h",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
# p.stdout.read()

#调用subprocess.run(...)是推荐的常用方法

