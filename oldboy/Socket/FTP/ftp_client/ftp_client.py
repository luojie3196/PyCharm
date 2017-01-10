#!/usr/bin/python
# encoding:utf-8

import socket
import os
import sys
import hashlib
import json
import time


class FtpClient(object):

    def __init__(self):
        self.client = socket.socket()
        self.home_path = ''
        self.current_path = ''
        self.user_space = 0
        self.overridden = False

    def help(self):
        msg = '''Usage: \n*ls [path] \n*cd [path] \n*get filename \n*put filename
        '''
        print(msg)

    def connect(self, ip, port):
        self.client.connect((ip, port))

    def close(self):
        self.client.close()

    def authentication(self):
        # 为了调试方便，暂时把登录认证关闭
        # username = input("User name: ").strip()
        # password = input("Password: ").strip()
        username = "test"
        password = "123"
        m = hashlib.md5()
        m.update(password.encode("utf-8"))
        password = m.hexdigest()
        msg_dic = {
            "action": "authentication",
            "username": username,
            "password": password
        }
        # 发送命令到服务器
        self.client.send(json.dumps(msg_dic).encode("utf-8"))
        print("cmd_auth-send ", msg_dic)
        server_res = self.client.recv(1024)
        user_dic = json.loads(server_res.decode())
        print("user dic:", user_dic)
        if user_dic["status"] == "NOK":
            return False
        self.home_path = user_dic["home_path"]
        self.current_path = self.home_path
        self.user_space = user_dic["space"]
        if user_dic["overridden"] == "True":
            self.overridden = True
        return True

    def interactive(self):
        if not self.authentication():
            print("Authentication failed")
            return False
        print("Authentication success")
        while True:
            cmd = input(">>").strip()
            if len(cmd) == 0:
                continue
            cmd_str = cmd.split()[0]
            if hasattr(self, "cmd_%s" % cmd_str):
                func = getattr(self, "cmd_%s" % cmd_str)
                func(cmd)
            else:
                self.help()

    def generator(self, file_size):
        size = 0
        while True:
            recv_size = yield
            percentage = int(recv_size / file_size * 100)
            if percentage != size:
                sys.stdout.write('\r' + '-' * percentage + '> ' + str(percentage) + '%')
                sys.stdout.flush()
                size = percentage

    def cmd_cd(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) == 1:
            path = self.home_path
        else:
            path = cmd_split[1]

        msg_dic = {
            "action": "cd",
            "path": path,
            "current_path": self.current_path,
            "home_path": self.home_path
        }
        # 发送命令到服务器
        self.client.send(json.dumps(msg_dic).encode("utf-8"))
        print("cmd_cd-send ", msg_dic)
        server_response = self.client.recv(1024)
        msg_dic = json.loads(server_response.decode())
        self.current_path = msg_dic["current_path"]
        status = msg_dic["status"]
        if status == "OK":
            print("current path:", self.current_path)
        else:
            print("No such file or directory")

    def cmd_ls(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) == 1:
            path = self.current_path
        else:
            path = os.path.join(self.current_path, cmd_split[1])

        msg_dic = {
            "action": "ls",
            "path": path
        }
        # 发送命令到服务器
        self.client.send(json.dumps(msg_dic).encode("utf-8"))
        print("cmd_ls-send ", msg_dic)
        # 接收命令的长度
        server_response = self.client.recv(1024)
        recv_dic = json.loads(server_response.decode())
        str_size = recv_dic["size"]
        status = recv_dic["status"]
        # 防止粘包
        self.client.send(b"Ready receive")
        recv_size = 0
        recv_data = b""
        while recv_size < str_size:
            if str_size - recv_size < 1024:
                size = 1024
            else:
                size = str_size - recv_size
            data = self.client.recv(size)
            recv_size += len(data)
            recv_data += data
        else:
            # 若status为0代表ls命令执行正确
            if not status:
                show_data = recv_data.decode()
                if os.path.isfile(show_data):
                    show_data = cmd_split[1]
                print(show_data)
            else:
                print("ls: cannot access %s: No such file or directory" % cmd_split[1])

    def cmd_put(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                pass
                # 文件大小和文件名组合成字典用json.dumps() send给server
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action": "put",
                    "filename": filename,
                    "size": filesize,
                    "current_path": self.current_path,
                    "home_path": self.home_path,
                    "user_space": self.user_space,
                    "overridden": self.overridden
                }
                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                print("cmd_put-send ", msg_dic)
                # 防止粘包，等服务器确认,用于确认剩余空间够不够
                server_response = self.client.recv(1024)
                status_dic = json.loads(server_response.decode())
                space_status = status_dic["space_status"]
                if space_status:
                    recv_size = 0
                    # 创建一个生成器，用于实现put过程的进度条
                    generator = self.generator(filesize)
                    generator.__next__()
                    m = hashlib.md5()
                    f = open(filename, "rb")
                    for line in f:
                        m.update(line)
                        self.client.send(line)
                        recv_size += len(line)
                        generator.send(recv_size)
                    else:
                        print("\nUpload size: ", recv_size)
                        f.close()
                        md5_str = self.client.recv(1024)
                        recv_md5 = md5_str.decode()
                        file_md5 = m.hexdigest()
                        if file_md5 == recv_md5:
                            print("%s file put success..." % filename)
                            # print("md5: %s" % m.hexdigest())
                            self.client.send(b"OK")
                        else:
                            print("MD5 check failed...")
                            print("%s file put failed..." % filename)
                            self.client.send(b"NOK")
                else:
                    print("Server no enough space")
            else:
                print(filename, "is not exist")

    def cmd_get(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            msg_dic = {
                "action": "get",
                "filename": filename,
                "current_path": self.current_path
            }
            self.client.send(json.dumps(msg_dic).encode("utf-8"))
            print("cmd_get-send ", msg_dic)
            server_response = self.client.recv(1024)
            msg_dic = json.loads(server_response.decode())
            file_status = msg_dic["file_status"]
            self.client.send(b"Ready to receive...")
            if file_status:
                file_size = msg_dic["file_size"]
                recv_size = 0
                # 创建一个生成器，用于实现get过程的进度条
                generator = self.generator(file_size)
                generator.__next__()
                m = hashlib.md5()
                f = open(filename, "wb")
                while recv_size < file_size:
                    if file_size - recv_size > 1024:
                        size = 1024
                    else:
                        size = file_size - recv_size
                        # print("Last recv size: ", size)
                    data = self.client.recv(size)
                    f.write(data)
                    m.update(data)
                    recv_size += len(data)
                    generator.send(recv_size)
                else:
                    f.close()
                    file_md5 = m.hexdigest()
                    self.client.send(file_md5.encode("utf-8"))
                    md5_check_status = self.client.recv(1024).decode()
                    if md5_check_status == "OK":
                        print("\nDownload size: ", recv_size)
                        print("%s file get success..." % filename)
                    else:
                        print("%s file get failed..." % filename)
                        os.remove(filename)
            else:
                print("Server didn't exist [%s] file" % filename)

ftp = FtpClient()
ftp.connect("localhost", 9999)
ftp.interactive()
ftp.close()
