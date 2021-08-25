import socketserver
import threading

class MyHandler(socketserver.BaseServer):  
    def handle(self):
        print(self.server,self.get_request,self.client_address)
        print('{}handle'.format(self.__class__))
        print(self.__dict__)
        print(type(self).__dict__)
        print(self.__class__.__base__[0].__dict__)
        print(threading.enumerate(),threading.current_thread())
        for i in range(3):
            data = self.request_queue_size(1024)
            print(data)
        print('End')


addr=('127.0.0.1',9000)
server =socketserver.ThreadingTCPServer(addr,MyHandler)

server.serve_forever()