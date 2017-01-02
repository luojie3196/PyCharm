#!/usr/bin/python
# encoding:utf-8

import subprocess


# Py2.7
subprocess.call("df -h", shell=True)  # 无法获取执行结果
a = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
# 一定要加管道才能获取到结果
# shell = True, 允许shell命令是字符串形式
a.stdout.read()

# subprocess.check_call() / subprocess.check_output()

# Py3.5
subprocess.run()
