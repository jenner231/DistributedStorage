import socket
import random


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

if __name__ == "__main__":
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            typ = input("Press 1 if you want to send a message to the server, or 2 if you want to send arbitrary binary data: ")
            print("Connected to the server successfully.")
            print(type(typ))
            message = ""
            #n = 0
            if typ == MESSAGE_STRING:
                message = typ.encode() + input("Enter a message to send to the server: ").encode()
                message = message[:4096]
                print(typ)                
            elif typ == MESSAGE_DATA:
                n = random.randint(1, 255)
                print("Sent {} bytes".format(n))
                message = typ.encode() + random.randbytes(n)
                print(typ)
            elif typ == MESSAGE_DATA_2:
                n = random.randint(1, 65535)
                print("Sent {} bytes".format(n))
                message = typ.encode() + random.randbytes(n)
                print(typ)
            elif typ == MESSAGE_DATA_3:
                n = random.randint(1, 16777215)
                print("Sent {} bytes".format(n))
                message = typ.encode() + random.randbytes(n)
                print(typ)
            else:
                print("Invalid input. Please enter a valid input.")
                continue
            
            s.connect(('127.0.0.1', 9000))
            s.sendall(message) #already encoded in the individual cases
            s.shutdown(socket.SHUT_WR)
            mes_rec = recv_all(s, 4096)
            mes_rec = mes_rec.decode()
            print(f"Received from server: {mes_rec}")
            s.close()