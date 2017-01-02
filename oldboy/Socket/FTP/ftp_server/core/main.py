#!/usr/bin/python
# encoding:utf-8

import socketserver
import json
import os


class MyTCPHandler(socketserver.BaseRequestHandler):

    def put(self, *args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        filesize = cmd_dic["size"]
        if os.path.isfile(filename):
            f = open(filename + ".new", "wb")
        else:
            f = open(filename, "wb")
        self.request.send(b"200 OK")
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print("File [%s] has uploaded ..." % filename)

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
