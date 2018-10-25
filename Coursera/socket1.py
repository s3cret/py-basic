#!/usr/local/bin/python3
import socket
# init socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# parameter to socket.connect() is tuple (hostname, port)
mysock.connect(('data.pr4e.org', 80))
# \r\n move the cusor, return and next line
message = 'GET http://data.pr4ee.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(message)

while True:
    # set the receive buffer
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    # decode the outside world utf-8 to python inside world unicode
    print(data.decode())
    #print(data)

    # close socket
mysock.close()
