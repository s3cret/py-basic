#!/usr/local/bin/python3
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
message = 'GET http://data.pr4ee.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(message)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
    #print(data)
mysock.close()
