#!/usr/bin/env python3

import socket
import time

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            full_data = b""
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data: break
                full_data += data
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# address = ("", 8001)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.bind(address)
# sock.listen(1)

# while True:
#     connection, client_address = sock.accept()
#     print(connection)
#     print(client_address)
#     all_result = b""
#     result = connection.recv(10000)
#     all_result += result
#     while (len(result) > 0):
#         #print(result)
#         result = connection.recv(10000)
#         all_result += result
#         #print(all_result)
#     print(all_result)
#     connection.sendall(all_result)
#     connection.close()

if __name__ == "__main__":
    main()