#!/usr/bin/python
# encoding:utf-8

import socket

client = socket.socket()
client.connect(("localhost", 6969))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode("utf-8"))
    data_size = client.recv(1024)
    client.send("Ready to receive now".encode("utf-8"))
    recv_data_size = 0
    recv_data = b""
    print(int(data_size.decode()))
    while recv_data_size < int(data_size.decode()):
        data = client.recv(1024)
        recv_data_size += len(data)
        recv_data += data
    else:
        print("cmd response done...",recv_data_size)
        print(recv_data.decode())

client.close()