#!/usr/bin/python
# encoding:utf-8

import socket
import hashlib

client = socket.socket()
client.connect(("localhost", 6969))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    # if cmd.split()[0] == "get":
    if cmd.startswith("get"):
        client.send(cmd.encode("utf-8"))
        data_size = client.recv(1024)
        client.send("Ready to receive now".encode("utf-8"))
        file_total_size = int(data_size.decode())
        filename = cmd.split()[1]
        recv_data_size = 0
        recv_data = b""
        print(file_total_size)
        f = open(filename + "_new", "wb")
        m = hashlib.md5()
        while recv_data_size < file_total_size:
            # size = file_total_size - recv_data_size
            if file_total_size - recv_data_size > 1024:
                size = 1024
            else:
                size = file_total_size - recv_data_size
                print("size: ", size)
            data = client.recv(size)
            recv_data_size += len(data)
            f.write(data)
            m.update(data)
            # print(file_total_size, recv_data_size)
        else:
            new_file_md5 = m.hexdigest()
            print("Receive file done...",recv_data_size)
            f.close()
        server_file_md5 = client.recv(1024).decode()
        print("Server file md5: ", server_file_md5)
        print("Client file md5: ", new_file_md5)

client.close()