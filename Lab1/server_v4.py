import socket
import threading
import random
import string

def handle_connection(c, a):
    print('Received Information from {}:'.format(a))
    message = c.recv(4096)
    try:
        message = message.decode()
        print("Received string")
        print(f'Message from {a}: {message}')
        c.send(f'Message: {message}'.encode())
    except UnicodeDecodeError: #If we cant decode the message, it is probably bytes
        print("Received bytes")
        #store in a file
        file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
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