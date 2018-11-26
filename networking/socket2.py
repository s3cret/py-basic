'''TCP servers:
As for the client, just use linux command nc or ncat
It's not worth it to write a python-client.
'''
import socket
import time
import threading

# you are going to talk to the outside world
# so do a encode before you send it
# and do a decode after you receive it
def tcplink(sock, addr):
    print('Accept new connection %s:%s' % addr)
    sock.send('Welcome!\n'.encode())
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        # exit not working because your received data contains
        # '\n' character, you should strip() it out
        if data.decode().strip() == 'exit' or not data:
            break
        sock.send('I gottya, %s'.encode() % data)
    sock.close()
    print('Connection from %s:%s closed' % addr)


# declare localhost
localhost = ('127.0.0.1', 9999)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(localhost)
socket.listen(2)

print('The socket starts listening.')
while True:
    sock, addr = socket.accept()
    # use multi-thread to handle multi-client access
    thread = threading.Thread(target=tcplink, args=(sock, addr))
    thread.start()
socket.close()

