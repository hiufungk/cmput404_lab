#!/usr/bin/env python3

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("", 8001)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    print(connection)
    print(client_address)
    all_result = b""
    result = connection.recv(10000)
    all_result += result
    while (len(result) > 0):
        #print(result)
        result = connection.recv(10000)
        all_result += result
        #print(all_result)
    connection.sendall(all_result)
    connection.close()
