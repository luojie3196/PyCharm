#!/usr/bin/python
# encoding:utf-8

import socketserver
import json
import os
import subprocess
import hashlib
import re


class MyTCPHandler(socketserver.BaseRequestHandler):

    def get_space(self, path):
        ret = subprocess.Popen("df %s | tail -1" % path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        ret_str = ret.stdout.read()
        left_space = ret_str.decode().split()[3]
        return int(left_space) * 1024

    def cd(self, *args):
        cmd_dic = args[0]
        path = cmd_dic["path"]
        current_path = cmd_dic["current_path"]
        home_path = cmd_dic["home_path"]
        tmp_path = current_path
        reg = re.findall(r'\s*\.\.\s*', path)
        n = 0
        while n < len(reg):
            if len(current_path) <= len(home_path):
                current_path = home_path
                break
            else:
                current_path = os.path.dirname(current_path)
            n += 1
        path = re.sub(r'\s*\.\.\s*', "", path)
        print("path:", path)
        # 增加replace方法解决windows下不能join问题
        current_path = current_path.replace("\\", "/")
        print("current path:", current_path)
        # current_path = os.path.join(current_path, path)
        current_path = current_path + "/" + path
        if os.path.isdir(current_path):
            status = "OK"
        else:
            status = "NOK"
            current_path = tmp_path
        print("current path:", current_path)
        msg_dic = {
            "status": status,
            "current_path": current_path
        }
        self.request.send(json.dumps(msg_dic).encode("utf-8"))

    def ls(self, *args):
        cmd_dic = args[0]
        path = cmd_dic["path"]
        cmd_res = os.popen("ls %s" % path).read()
        cmd_size = str(len(cmd_res.encode("utf-8")))
        self.request.send(cmd_size.encode("utf-8"))
        # 防止粘包
        self.request.recv(1024)
        self.request.send(cmd_res.encode("utf-8"))

    def get(self, *args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        if os.path.isfile(filename):
            file_status = True
            file_size = os.stat(filename).st_size
        else:
            file_status = False
            file_size = None
        msg_dic = {
            "file_status": file_status,
            "file_size": file_size
        }
        self.request.send(json.dumps(msg_dic).encode("utf-8"))
        self.request.recv(1024)
        if file_status:
            m = hashlib.md5()
            f = open(filename, "rb")
            for line in f:
                self.request.send(line)
                m.update(line)
            else:
                f.close()
                md5_str = self.request.recv(1024)
                recv_md5 = md5_str.decode()
                file_md5 = m.hexdigest()
                if file_md5 == recv_md5:
                    print("%s file get success..." % filename)
                    # print("md5: %s" % m.hexdigest())
                    self.request.send(b"OK")
                else:
                    print("MD5 check failed...")
                    print("%s file get failed..." % filename)
                    self.request.send(b"NOK")
                # print("[%s] file send success..." % filename)
            f.close()
        else:
            print("[%s] file not exist" % filename)

    def put(self, *args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        file_size = cmd_dic["size"]
        overridden = cmd_dic["overridden"]
        # TODO: 如何动态传入path值
        left_space = self.get_space(".")
        print("left_space: ", left_space)
        print("file size: ", file_size)
        if left_space < file_size:
            space_status = False
        else:
            space_status = True
        print("space_status: ", space_status)
        msg_dic = {
            "space_status": space_status
        }
        self.request.send(json.dumps(msg_dic).encode("utf-8"))
        if space_status:
            if os.path.isfile(filename) and not overridden:
                f = open(filename + ".new", "wb")
            else:
                f = open(filename, "wb")
            recv_size = 0
            m = hashlib.md5()
            while recv_size < file_size:
                if file_size - recv_size > 1024:
                    size = 1024
                else:
                    size = file_size - recv_size
                    print("Last recv size: ", size)
                data = self.request.recv(size)
                f.write(data)
                m.update(data)
                recv_size += len(data)
            else:
                f.close()
                file_md5 = m.hexdigest()
                self.request.send(file_md5.encode("utf-8"))
                md5_check_status = self.request.recv(1024).decode()
                print("md5_check_status: ", md5_check_status)
                if md5_check_status == "OK":
                    print("%s file put success..." % filename)
                    # print("md5: %s" % m.hexdigest())
                else:
                    print("%s file put failed..." % filename)
                    os.remove(filename)

        else:
            print("No space left on device")

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
            except ConnectionResetError as e:
                print("err: ", e)
                break
            else:
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self, action):
                    func = getattr(self, action)
                    func(cmd_dic)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  # 多并发
    server.serve_forever()
