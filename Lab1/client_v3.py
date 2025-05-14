import socket




if __name__ == "__main__":
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            input("Press Enter to connect to the server...")
            
            print("Connected to the server successfully.")
            s.connect(('127.0.0.1', 9000))
            message = input("Enter a message to send to the server: ")
            message = message[:4096]
            s.send(message.encode())
            mes_rec = s.recv(4096).decode()
            print(f"Received from server: {mes_rec}")
            s.close()