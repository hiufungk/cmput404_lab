#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('www.google.com', 80)
sock.connect(address)
request = b"GET / HTTP/1.0\n\n"
sock.sendall(request)

all_result = b""
result = sock.recv(10000)
while (len(result) > 0):
    #print(result)
    result = sock.recv(10000)
    all_result += result
print(all_result)