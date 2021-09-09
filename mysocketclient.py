import socket
import threading
import os
import time

class mytcpclient():
    def __init__(self):
        self.running = False
        self.sock = socket.socket()

    def open(self,host_ip,host_port):
        threading.Thread.__init__(self)
        try:
            self.sock.connect((host_ip, host_port))
            self.sock.accept()
        except socket.error as e:
            return("Socket Connect Error:%s" % e)
            exit(1)
        self.running = True
        self.error_cnt = 0
        return("connect success")

    def close(self):
        self.sock.close()

    def myrecv(self):
        myrecv=self.sock.recv(1024).decode(encoding='gbk')
        return myrecv
    def start(self):
        t=threading.Thread(target=self.myrecv)
        t.start()

    def send(self,data):
        while self.running:
            try:
                send_data = '\x12\x34\x56'
                self.sock.send(send_data)
                data = self.sock.recv(1024)
                if len(data) > 0:
                    self.error_cnt = 0
                    recv_data = data.encode('hex')
                    print ('recv:', recv_data)
                sleep(1)

            except socket.error as e:
                print ('socket running error:', str(e))
                break

        print ('SockClient Thread Exit\n')


        