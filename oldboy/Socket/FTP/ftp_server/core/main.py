#!/usr/bin/python
# encoding:utf-8

import socketserver
import json
import os
import subprocess
import hashlib
import re


class MyTCPHandler(socketserver.BaseRequestHandler):

    def get_used_space(self, path):
        ret = subprocess.Popen("du -sh %s" % path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        ret_str = ret.stdout.read()
        used_space = ret_str.decode().split()[0]
        return used_space

    def authentication(self, *args):
        userinfo_dic = args[0]
        username = userinfo_dic["username"]
        password = userinfo_dic["password"]
        with open("../conf/userinfo.json", "r") as fr:
            userinfo = json.loads(fr.read())["UserInfo"]
        msg_dic = {
            "status": "NOK"
        }
        for user in userinfo:
            if user["Name"] == username and user["PWD"] == password:
                msg_dic = {
                    "status": "OK",
                    "home_path": user["HomeDir"],
                    "space": user["Space"],
                    "overridden": user["overridden"]
                }
                break
        print("msg_dic: ", msg_dic)
        self.request.send(json.dumps(msg_dic).encode("utf-8"))

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
        current_path = current_path.replace("\\", "/")
        print("current path:", current_path)
        print("home path:", home_path)
        if path != home_path:
            current_path = current_path + "/" + path
        else:
            current_path = home_path
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
        status, output = subprocess.getstatusoutput("ls %s" % path)
        cmd_size = len(output.encode("utf-8"))
        msg_dic = {
            "status": status,
            "size": cmd_size
        }
        self.request.send(json.dumps(msg_dic).encode("utf-8"))
        # 防止粘包
        self.request.recv(1024)
        self.request.send(output.encode("utf-8"))

    def get(self, *args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        current_path = cmd_dic["current_path"]
        file_full_path = current_path + "/" + filename
        if os.path.isfile(file_full_path):
            file_status = True
            file_size = os.stat(file_full_path).st_size
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
            f = open(file_full_path, "rb")
            for line in f:
                self.request.send(line)
                m.update(line)
            else:
                f.close()
                md5_str = self.request.recv(1024)
                recv_md5 = md5_str.decode()
                file_md5 = m.hexdigest()
                if file_md5 == recv_md5:
                    print("%s file get success..." % file_full_path)
                    # print("md5: %s" % m.hexdigest())
                    self.request.send(b"OK")
                else:
                    print("MD5 check failed...")
                    print("%s file get failed..." % file_full_path)
                    self.request.send(b"NOK")
                # print("[%s] file send success..." % filename)
            f.close()
        else:
            print("[%s] file not exist" % file_full_path)

    def put(self, *args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        file_size = cmd_dic["size"]
        current_path = cmd_dic["current_path"]
        home_path = cmd_dic["home_path"]
        overridden = cmd_dic["overridden"]
        # 获取用户分配的空间
        user_space = cmd_dic["user_space"]
        user_space = re.sub(r"\D", "", user_space)
        user_space = int(user_space)*1024*1024
        # 获取已使用空间
        used_space = self.get_used_space(home_path)
        used_space = re.sub(r"\D", "", used_space)
        used_space = int(used_space) * 1024 * 1024
        # 获取可用空间并与需上传的文件比较
        available_space = user_space - used_space
        print("available_space: ", available_space)
        print("file size: ", file_size)
        if available_space < file_size:
            space_status = False
        else:
            space_status = True
        print("space_status: ", space_status)
        msg_dic = {
            "space_status": space_status
        }
        self.request.send(json.dumps(msg_dic).encode("utf-8"))
        file_full_path = current_path + "/" + filename
        if space_status:
            if os.path.isfile(file_full_path) and not overridden:
                f = open(file_full_path + ".new", "wb")
            else:
                f = open(file_full_path, "wb")
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
                    print("%s file put success..." % file_full_path)
                    # print("md5: %s" % m.hexdigest())
                else:
                    print("%s file put failed..." % file_full_path)
                    os.remove(file_full_path)

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
