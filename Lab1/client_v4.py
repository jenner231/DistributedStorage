import socket
import random




if __name__ == "__main__":
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            typ = input("Press 1 if you want to send a message to the server, or 2 if you want to send arbitrary binary data: ")
            print("Connected to the server successfully.")
            print(type(typ))
            message = ""
            if typ == '1':
                message = input("Enter a message to send to the server: ")                
            elif typ == '2':
                message = random.randbytes(4096)
                print(type(message))
            else:
                print("Invalid input. Please enter 1 or 2.")
                continue
            message = message[:4096]
            s.connect(('127.0.0.1', 9000))
            
            if typ == '1': 
                s.send(message.encode()) 
            else: 
                s.send(message)
            mes_rec = s.recv(4096).decode()
            print(f"Received from server: {mes_rec}")
            s.close()