import socket
# the socket.SOCK_DGRAM indicates that it is a UDP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
localhost = ('127.0.0.1', 9999)
socket.bind(localhost)
# do not need to call socket.listen()
print('UDP server start:')
while True:
    data, addr = socket.recvfrom(1024)
    print('Received from %s:%s', addr)
    socket.sendto('I gottya %s' % data)

