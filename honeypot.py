import socketserver
import logging

import threading
import socket

logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s', )


class SocketListener(socketserver.BaseRequestHandler):
    def handle(self):
        self.logger.debug('handle')
        data = self.request.recv(1024)
        self.request.send(data)
        print(data.decode())
        return

    def __init__(self, request, src_address, server):
        self.logger = logging.getLogger('SocketListener')
        socketserver.BaseRequestHandler.__init__(self, request, src_address, server)

class ThreadListener(threading.Thread):
    def __init__(self):
        print("init")

def main():
    port = 23
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('', port), SocketListener)
    server.serve_forever()


if __name__ == '__main__':
    main()
