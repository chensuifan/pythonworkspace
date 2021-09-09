
import socketserver
import threading

class myhandler(socketserver.BaseRequestHandler):
    def setup(self):
        super().setup()
        self.event=threading.Event()

    def handle(self):
        super().handle()
        while not self.event.wait(1):
            print('!!!!!!')


# 啓動服務
addr=('127.0.0.1',9999)
server=socketserver.ThreadingTCPServer(addr,myhandler)

server.serve_forever()

server.server_close()