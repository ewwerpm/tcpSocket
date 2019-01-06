#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socketserver
import subprocess

##  代号 地址和端口 连接对象
class myconn(object):   ##存放连接
    listconn = {}  ##  地址端口  连接对象
    # codeflage = {}  ##  代号   地址端号


class MyServer(socketserver.BaseRequestHandler):

    def setup(self):
        myconn.listconn[self.client_address] = self.request
        pass

    def handle(self):
        print("got connection from",self.client_address)
        while True:
            conn = self.request
            data = conn.recv(1024)
            if not data:
                break
            print('****************')
            print(data)

            #如果目标客户端在发送数据给目标客服端
            # 这里可以根据对方的ip和端口号来查找 我这里直接发给每一个用户了
            print(len(myconn.listconn))
            if len(myconn.listconn) > 1:
                for i in myconn.listconn.keys():
                    print(i)
                    print(self.client_address)
                    if self.client_address != i:
                        print(i[1])
                        #if (str(i[1]) in data.decode("utf-8")):   有用
                        str1=data.decode("utf-8")
                        print(str1+"$$$$$")
                        str2=':'
                        print(str1.index(str2))
                        print("*****")
                        if(int(str1[0:str1.index(':')])==i[1]):
                            #if (i[1] == data.decode("utf-8")[1:6]):
                            myconn.listconn[i].sendall(data)
                pass
            else: ##不再      则发送数据给客户端
                conn.sendall(data)
                pass
            #conn.sendall(data)

    def finish(self):
        del myconn.listconn[self.client_address]
        pass
    pass

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('localhost',8022),MyServer)
    print('waiting for connection...')
    server.serve_forever()