#!/usr/bin/python
# encoding:utf-8

import socket
import os
import hashlib
import json


class FtpClient(object):

    def __init__(self):
        self.client = socket.socket()
        pass

    def help(self):
        msg = '''
        ls
        pwd
        cd ../..
        get filename
        put filename
        '''
        print(msg)

    def connect(self, ip, port):
        self.client.connect((ip, port))
        pass

    def interactive(self):
        while True:
            # self.authenticate()
            cmd = input(">>").strip()
            if len(cmd) == 0:
                continue
            cmd_str = cmd.split()[0]
            if hasattr(self, "cmd_%s" % cmd_str):
                func = getattr(self, "cmd_%s" % cmd_str)
                func(cmd)
            else:
                self.help()

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
                    "overridden": True
                }
                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                print("cmd_put-send ", msg_dic)
                # 防止粘包，等服务器确认,用于确认剩余空间够不够
                server_response = self.client.recv(1024)
                status_dic = json.loads(server_response.decode())
                space_status = status_dic["space_status"]
                if space_status:
                    m = hashlib.md5()
                    f = open(filename, "rb")
                    for line in f:
                        m.update(line)
                        self.client.send(line)
                    else:
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
                    print("Server not enough space")
            else:
                print(filename, "is not exist")

    def cmd_get(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            msg_dic = {
                "action": "get",
                "filename": filename,
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
                m = hashlib.md5()
                f = open(filename, "wb")
                while recv_size < file_size:
                    if file_size - recv_size > 1024:
                        size = 1024
                    else:
                        size = file_size - recv_size
                        print("Last recv size: ", size)
                    data = self.client.recv(size)
                    f.write(data)
                    m.update(data)
                    recv_size += len(data)
                else:
                    f.close()
                    file_md5 = m.hexdigest()
                    self.client.send(file_md5.encode("utf-8"))
                    md5_check_status = self.client.recv(1024).decode()
                    print("md5_check_status: ", md5_check_status)
                    if md5_check_status == "OK":
                        print("%s file get success..." % filename)
                        # print("md5: %s" % m.hexdigest())
                    else:
                        print("%s file get failed..." % filename)
                        os.remove(filename)
            else:
                print("Server didn't exist [%s] file" % filename)

ftp = FtpClient()
ftp.connect("localhost", 9999)
ftp.interactive()
