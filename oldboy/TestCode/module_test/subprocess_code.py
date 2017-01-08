#!/usr/bin/python
# -*- coding:utf-8 -*-


import subprocess

# obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# obj.stdin.write('print([1,2,3,4,5])'.encode('utf-8'))
#
# out_error_list = obj.communicate(timeout=10)
# print(out_error_list)


# 实现su自动登录
def mypass():
    mypass = '123'  # or get the password from anywhere
    return mypass


echo = subprocess.Popen(['echo', mypass()],
                        stdout=subprocess.PIPE,
                        )

sudo = subprocess.Popen(['sudo', '-S', 'iptables', '-L'],
                        stdin=echo.stdout,
                        stdout=subprocess.PIPE,
                        )

end_of_pipe = sudo.stdout

print("Password ok \n Iptables Chains %s" % end_of_pipe.read())