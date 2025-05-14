import socket
import threading
import random
import string

#String message
MESSAGE_STRING = '1'

#Data message, data size encoded on 1 byte (data size: up to 255 bytes)
MESSAGE_DATA = '2'

#Data message, data size encoded on 2 bytes (data size: up to 64kB bytes)
MESSAGE_DATA_2 = '3'

#Data message, data size encoded on 3 bytes (data size: up to 16 MB bytes)
MESSAGE_DATA_3 = '4'

def recv_all(sock, chunk_size):
    data = bytearray()
    while True:
        chunk = sock.recv(chunk_size)
        if not chunk:
            break
        data.extend(chunk)
    return bytes(data)


def handle_connection(c, a):
    print('Received Information from {}:'.format(a))
    message = recv_all(c, 4096)
    typ = message[:1].decode()
    message = message[1:]

    if typ == MESSAGE_STRING:
        message.decode()
        print("Received string")
        print(f'Message from {a}: {message}')
        c.send(f'Message: {message}'.encode())
    elif typ == MESSAGE_DATA:
        print("Received {} bytes", len(message))
        #store in a file
        file_name = typ.join(random.choice(string.ascii_lowercase) for i in range(16))
        with open(file_name+'.txt', 'wb') as f:
            f.write(message)
        c.send(f'Message: {message}'.encode())
        print('Sent Bytes back to client')
    elif typ == MESSAGE_DATA_2:
        print("Received {} bytes", len(message))
        #store in a file
        file_name = typ.join(random.choice(string.ascii_lowercase) for i in range(16))
        with open(file_name+'.txt', 'wb') as f:
            f.write(message)
        c.send(f'Message: {message}'.encode())
        print('Sent Bytes back to client')
    elif typ == MESSAGE_DATA_3:
        print("Received {} bytes", len(message))
        #store in a file
        file_name = typ.join(random.choice(string.ascii_lowercase) for i in range(16))
        with open(file_name+'.txt', 'wb') as f:
            f.write(message)
        c.send(f'Message: {message}'.encode())
        print('Sent Bytes back to client')


    c.close()


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9000))
    s.listen(5)
    while True:
        #start new thread for each connection
        (c, a) = s.accept()
        thread = threading.Thread(target=handle_connection, args=(c, a))
        thread.start()