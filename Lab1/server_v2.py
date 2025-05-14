import socket
import threading

def handle_connection(c, a):
    print('Received Information from {}:'.format(a))
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