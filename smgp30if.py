import sys
import socket
import time
import threading
import random


start_time = time.time()

class mythread(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self)
        self._run_num = loopnum
        self.sleepTime = random.randint(1,5)


    def run(self):
        global count, mutex
        threadname = threading.currentThread().getName()
        time.sleep(self.sleepTime)



        for i in range(int(self._run_num)):
            #get lock
           # mutex.acquire()
            count = count + 1
            #release lock
           # mutex.release()

            mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock.connect(('10.137.73.90',10891))
            #mysock.send('\x00\x00\x00\x2A\x00\x00\x00\x01\x00\x00\x00\x01\x53\x50\x00\x00\x00\x00\x00\x00\x54\xC6\xA1\x62\x8C\xA3\x80\x10\x4A\x17\x72\x41\xC0\xCC\x3E\x2D\x00\x12\x20\xF8\x68\x30')
            #rdata = mysock.recv(100)
            #print  i, 'received:', rdata
    
    #=====10 SMGP sockets :socket1..socket10       
            mysock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock1.connect(('10.137.73.90',10891))
            #mysock1.send('\x00\x00\x00\x2A\x00\x00\x00\x01\x00\x00\x00\x01\x53\x50\x00\x00\x00\x00\x00\x00\x54\xC6\xA1\x62\x8C\xA3\x80\x10\x4A\x17\x72\x41\xC0\xCC\x3E\x2D\x00\x12\x20\xF8\x68\x30')
            #rdata = mysock.recv(100)
  
         
            mysock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock2.connect(('10.137.73.90',10891))
            #mysock2.send('\x00\x00\x00\x2A\x00\x00\x00\x01\x00\x00\x00\x01\x53\x50\x00\x00\x00\x00\x00\x00\x54\xC6\xA1\x62\x8C\xA3\x80\x10\x4A\x17\x72\x41\xC0\xCC\x3E\x2D\x00\x12\x20\xF8\x68\x30')
            #rdata = mysock.recv(100)
        
            mysock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock3.connect(('10.137.73.90',10891))
            #mysock3.send('\x00\x00\x00\x2A\x00\x00\x00\x01\x00\x00\x00\x01\x53\x50\x00\x00\x00\x00\x00\x00\x54\xC6\xA1\x62\x8C\xA3\x80\x10\x4A\x17\x72\x41\xC0\xCC\x3E\x2D\x00\x12\x20\xF8\x68\x30')
            #rdata = mysock.recv(100)
         
         
            mysock4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock4.connect(('10.137.73.90',10891))
            #mysock4.send('\x00\x00\x00\x2A\x00\x00\x00\x01\x00\x00\x00\x01\x53\x50\x00\x00\x00\x00\x00\x00\x54\xC6\xA1\x62\x8C\xA3\x80\x10\x4A\x17\x72\x41\xC0\xCC\x3E\x2D\x00\x12\x20\xF8\x68\x30')
            #rdata = mysock.recv(100)
         
            mysock5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock5.connect(('10.137.73.90',10891))
            #mysock5.send('\x00\x00\x00\x2A\x00\x00\x00\x01\x00\x00\x00\x01\x53\x50\x00\x00\x00\x00\x00\x00\x54\xC6\xA1\x62\x8C\xA3\x80\x10\x4A\x17\x72\x41\xC0\xCC\x3E\x2D\x00\x12\x20\xF8\x68\x30')
            #rdata = mysock.recv(100)
         
                    
            mysock6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock6.connect(('10.137.73.90',10891))
            #mysock6.send('\x00\x00\x00\x2A\x00\x00\x00\x01\x00\x00\x00\x01\x53\x50\x00\x00\x00\x00\x00\x00\x54\xC6\xA1\x62\x8C\xA3\x80\x10\x4A\x17\x72\x41\xC0\xCC\x3E\x2D\x00\x12\x20\xF8\x68\x30')
            #rdata = mysock.recv(100)
         
            mysock7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock7.connect(('10.137.73.90',10891))
            #mysock7.send('\x00\x00\x00\x2A\x00\x00\x00\x01\x00\x00\x00\x01\x53\x50\x00\x00\x00\x00\x00\x00\x54\xC6\xA1\x62\x8C\xA3\x80\x10\x4A\x17\x72\x41\xC0\xCC\x3E\x2D\x00\x12\x20\xF8\x68\x30')
            #rdata = mysock.recv(100)
         
            mysock8 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock8.connect(('10.137.73.90',10891))
            #mysock8.send('\x00\x00\x00\x2A\x00\x00\x00\x01\x00\x00\x00\x01\x53\x50\x00\x00\x00\x00\x00\x00\x54\xC6\xA1\x62\x8C\xA3\x80\x10\x4A\x17\x72\x41\xC0\xCC\x3E\x2D\x00\x12\x20\xF8\x68\x30')
            #rdata = mysock.recv(100)
         
            mysock9 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock9.connect(('10.137.73.90',10891))
            #mysock9.send('\x00\x00\x00\x2A\x00\x00\x00\x01\x00\x00\x00\x01\x53\x50\x00\x00\x00\x00\x00\x00\x54\xC6\xA1\x62\x8C\xA3\x80\x10\x4A\x17\x72\x41\xC0\xCC\x3E\x2D\x00\x12\x20\xF8\x68\x30')
            #rdata = mysock.recv(100)
         
            mysock10 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock10.connect(('10.137.73.90',10891))
            #mysock10.send('\x00\x00\x00\x2A\x00\x00\x00\x01\x00\x00\x00\x01\x53\x50\x00\x00\x00\x00\x00\x00\x54\xC6\xA1\x62\x8C\xA3\x80\x10\x4A\x17\x72\x41\xC0\xCC\x3E\x2D\x00\x12\x20\xF8\x68\x30')
            #rdata = mysock.recv(100)
         
         
 
    

            time.sleep(5)  
            
            #mysock1.send('\x00\x00\x00\x0C\x00\x00\x00\x06\x00\x00\x00\x02')
            #mysock2.send('\x00\x00\x00\x0C\x00\x00\x00\x06\x00\x00\x00\x02')
            #mysock3.send('\x00\x00\x00\x0C\x00\x00\x00\x06\x00\x00\x00\x02')
            #mysock4.send('\x00\x00\x00\x0C\x00\x00\x00\x06\x00\x00\x00\x02')
            #mysock5.send('\x00\x00\x00\x0C\x00\x00\x00\x06\x00\x00\x00\x02')
            #
            #mysock6.send('\x00\x00\x00\x0C\x00\x00\x00\x06\x00\x00\x00\x02')
            #mysock7.send('\x00\x00\x00\x0C\x00\x00\x00\x06\x00\x00\x00\x02')
            #mysock8.send('\x00\x00\x00\x0C\x00\x00\x00\x06\x00\x00\x00\x02')
            #mysock9.send('\x00\x00\x00\x0C\x00\x00\x00\x06\x00\x00\x00\x02')
            #mysock10.send('\x00\x00\x00\x0C\x00\x00\x00\x06\x00\x00\x00\x02')
            

            time.sleep(5)  
            
            #mysock.close()
            #mysock1.close()
            #mysock2.close()
            #mysock3.close()
            #mysock4.close()
            #mysock5.close()
            #          
            #mysock6.close()
            #mysock7.close()
            #mysock8.close()
            #mysock9.close()
            #mysock10.close()
            
            

            

if __name__ == "__main__":
    global count, mutex
    threads = []
    num =10
    loopnum=1000
    count = 1
    #create lock
 #   mutex = threading.Lock()
    for x in range(0, num):
        threads.append(mythread(10))

    for t in threads:
        t.start()
        
    for t in threads:
        t.join()

print "Elapsed Time: %s" % (time.time() - start_time)
