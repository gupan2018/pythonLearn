# -*- coding:utf-8 -*-
# __author__ = 'gupan'

'''
使用socketserver步骤：
'''

import socketserver

# 每一个请求过来都会实例化MyTCPHandler
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        '''
        handle中自己处理所有和客户端的交互
        :return:
        '''
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err: {error}".format(error=e))
                break

if __name__ == "__main__":
    HOST, PORT = "localhost", 6969

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
