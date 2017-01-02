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
                # TODO: 文件大小和文件名组合成字典用json.dumps() send给server
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action": "put",
                    "filename": filename,
                    "size": filesize,
                    "overridden": True
                }
                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                print("cmd_put-send ", msg_dic)
                # TODO: 防止粘包，等服务器确认,可用于确认剩余空间够不够
                server_response = self.client.recv(1024)
                # TODO: .....
                f = open(filename, "rb")
                for line in f:
                    self.client.send(line)
                else:
                    print("%s file upload success..." % filename)
                    f.close()
            else:
                print(filename, "is not exist")
                pass
        pass

    def cmd_get(self):
        pass

ftp = FtpClient()
ftp.connect("localhost", 9999)
ftp.interactive()