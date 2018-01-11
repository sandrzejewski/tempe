import socket
import sys


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('192.168.1.110', 10000))
    while 1:
        received, addr = sock.recvfrom(1024)
        print('Information: ', received.decode())
        print('Connection: ', addr)
    sock.close()


if __name__ == "__main__":
    main()
    
