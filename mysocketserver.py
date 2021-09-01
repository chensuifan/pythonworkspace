import threading
import time
import socket
import logging

logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='socketsever.log',
                    filemode='w')

class mysocketserver:
    
    def __init__(self,ip='127.0.0.1',port=9999):
        self.sock = socket.socket()
        self.addr=(ip,port)
        self.clients={}

    def _accept(self):
        conn,client=self.sock.accept()
        self.clients[client] = conn
        threading.Thread(target=self._recv,args=(conn,),name='recv').start()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        threading.Thread(target=self._accept,name='accept').start()

    def stop(self):
        for c in self.clients.values():
            c.close()
            self.clients.pop(c)
        self.sock.close()


    def _recv(self,conn):
        while True:
            try:
                data= conn.recv(1024)
            except Exception as e:
                conn.close()
                self.stop()
            
            logging.info(data.decode('utf-8'))
            # conn.send(data.decode('utf-8'))
            for a in self.clients.values():
                print(data.decode('utf-8'))


cs=mysocketserver()
cs.start()