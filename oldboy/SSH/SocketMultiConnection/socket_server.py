#!/usr/bin/python
# encoding:utf-8

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print("err: ", e)
                break
            # if not self.data:
            #     print(self.client_address, " unconnected...")
            #     break

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) # 多并发
    server.serve_forever()