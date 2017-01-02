#!/usr/bin/python
# encoding:utf-8

import socket
import os,time
import hashlib

server = socket.socket()
server.bind(("localhost", 6969))
server.listen()

while True:
    conn, addr = server.accept()
    print('New connected: ', addr)

    while True:
        try:
            recv_data = conn.recv(1024)
        except ConnectionResetError as e:
            print("Client unconnected")
            break
        recv_data = recv_data.decode("utf-8")
        print("cmd: ", recv_data)
        cmd, file_name = recv_data.split()
        if cmd == "get":
            if os.path.isfile(file_name):
                f = open(recv_data.split()[1], "rb")
                m = hashlib.md5()
                file_size = os.stat(file_name).st_size
                conn.send(str(file_size).encode("utf-8"))
                client_ack = conn.recv(1024)
                for line in f:
                    m.update(line)
                    conn.send(line)
                print("file md5: ", m.hexdigest())
                f.close()
                conn.send(m.hexdigest().encode("utf-8"))
            else:
                print("%s file not exist." % file_name)
        else:
            print("Nothing to do.")

server.close()