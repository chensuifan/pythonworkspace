import sys

import socket

import threading

from time import sleep


class SockClient(threading.Thread):

    def __init__(self, host_ip, host_port):
        threading.Thread.__init__(self)
        self.running = False
        self.sock = socket.socket()
        self.sock.settimeout(20)  # 20 seconds
        try:
            self.sock.connect((host_ip, host_port))
        except socket.error as e:
            print("Socket Connect Error:%s" % e)
            exit(1)
        print("connect success")
        self.running = True

        self.error_cnt = 0

    def run(self):

        while self.running:

            try:
                send_data = '\x12\x34\x56'
                self.sock.send(send_data.encode('gbk'))
                data = self.sock.recv(1024)
                if len(data) > 0:
                    self.error_cnt = 0
                    recv_data = data.encode('hex')
                    print('recv:', recv_data)

                sleep(1)

            except socket.error as e:
                print ('socket running error:', str(e))
                break

        print ('SockClient Thread Exit\n')

if __name__ == "__main__":

    sock_client = SockClient('192.168.10.1', 8080)

    sock_client.start()

    try:
        while True:
            sleep(1)

            if not sock_client.is_alive():
                break

    except KeyboardInterrupt:
        print ('ctrl+c')
        sock_client.running = False

    sock_client.join()
    print ('exit finally')
