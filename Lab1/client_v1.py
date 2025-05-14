import socket




if __name__ == "__main__":
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            input("Press Enter to connect to the server...")
            s.connect(('127.0.0.1', 9000))
            print("Connected to the server successfully.")
            s.close()