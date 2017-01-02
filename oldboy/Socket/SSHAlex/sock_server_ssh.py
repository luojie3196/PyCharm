#!/usr/bin/python
# encoding:utf-8


import socket
import os

server = socket.socket()
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 允许地址重用
server.bind(('localhost', 9999))
server.listen()

while True:
    conn, addr = server.accept()
    print('New conn: ', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('Client is unconnected')
            break
        print('cmd: ', data)
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = 'cmd has no output...'
        conn.send(str(len(cmd_res.encode('utf-8'))).encode('utf-8'))
        client_ack = conn.recv(1024) # 解决粘包问题
        conn.send(cmd_res.encode('utf-8'))

server.close()