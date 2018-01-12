import socket               # Import socket module


def main():
    sock = socket.socket()
    sock.settimeout(10240)
    sock.connect(("chat.freenode.net", 6667))
    #sock.send("USER guest tolmoon tolsun :Ronnie Reagan".encode())
    sock.send("NICK Ron343423423\r\n".encode())
    sock.send("USER user user user :Ronnie Regan\r\n".encode())
    sock.send("LIST\r\n".encode())
    while True:
        buffer = ''
        buffer += str(sock.recv(4096).decode())
        print(buffer)


if __name__ == '__main__':
    main()
