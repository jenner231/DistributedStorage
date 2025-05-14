import socket



if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9000))
    s.listen(5)
    while True:
        c, a = s.accept()
        print('Recevied Information from {}:'.format(a))
        c.close()