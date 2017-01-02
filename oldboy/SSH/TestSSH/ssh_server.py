#!/usr/bin/python
# encoding:utf-8

import socket
import os,time

server = socket.socket()
server.bind(("localhost", 6969))
server.listen()

while True:
    conn, addr = server.accept()
    print('New connected: ', addr)

    while True:
        # recv_data = conn.recv(1024)
        # if not recv_data:
        #     print("Client unconnected")
        #     break
        try:
            recv_data = conn.recv(1024)
        except ConnectionResetError as e:
            print("Client unconnected")
            break
        print("recv_data: ", recv_data.decode("utf-8"))
        cmd_res = os.popen(recv_data.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = "Invalid cmd..."
        # print("cmd str: ", cmd_res)
        data_size = str(len(cmd_res.encode("utf-8")))
        # print("data size: ", data_size)
        conn.send(data_size.encode("utf-8"))
        client_ack = conn.recv(1024)
        conn.send(cmd_res.encode("utf-8"))

server.close()