import socket
import keyboard
import os
import random


class Client:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock


    def connect(self, host, port):

        self.sock.connect((host,port))


    def send(self, msg):
        if msg:
            self.sock.send(bytes(msg, 'utf-8'))
        else:
            self.sock.send(bytearray(os.urandom(random.randrange(0, 10000))))


if __name__ == "__main__":
    client = Client()
    localhost = '127.0.0.1'
    port = 9000
    
    client.connect(localhost, port)

    while True:
        msg = input('Press 1 to send a string, press 2 to send binary data')
        client.send(str(msg))

        data = client.sock.recv(4096)
        print(data.decode())


    

