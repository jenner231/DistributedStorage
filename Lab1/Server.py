import socket
import threading
localhost = '127.0.0.1'

class Server:
    def __init__(self, host=localhost, port=9000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def handle_new_client(self, conn, addr):
        with conn:
            while True:
                data = conn.recv(4096)
                
                if len(data.decode()) > 0:
                    print(f'Received from {addr}: {data.decode()}')
                    conn.sendall(bytes(f'Received message: {data.decode()}', 'utf-8'))

    def start_server(self):
        #start
        self.server_socket.bind((self.host, self.port))
        print(f'Server started on {self.host}:{self.port}')

        #listen
        self.server_socket.listen()
        print('Listening, waiting for a connection')


        # Accept incoming connection
        while True:
            conn, addr = self.server_socket.accept()
            print(f'Received connection from {addr}')
            client_thread = threading.Thread(target=self.handle_new_client, args=(conn, addr))
            client_thread.start()

                
                



    def stop_connection(self):
        self.server_socket.close()
        print('Server stopped')


if __name__ == "__main__":
    server = Server()
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_connection()    