#!/usr/bin/python
# encoding:utf-8


import socket

client = socket.socket()
client.connect(('localhost', 9999))

while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024)
    print('cmd actual size: ', cmd_res_size)
    client.send('Ready to receive now'.encode('utf-8')) # 解决粘包问题
    receive_size = 0
    receive_data = b''
    while receive_size != int(cmd_res_size.decode()):
        data = client.recv(1024)
        receive_size += len(data)
        receive_data += data
    else:
        print('cmd res receive done...', receive_size)
        print(receive_data.decode())

client.close()