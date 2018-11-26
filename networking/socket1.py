import socket

# the socket.AF_INET stands for ipv4 protocol
# also ipv6 is represented by socket.AF_INET6
# with socket.SOCK_STREAM argument specified,
# the socket will use stream-orentied TCP
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ('www.sina.com.cn', 80)
# do connect(host) to connect socket to a specifed host
socket.connect(host)
# socket.send(byte utf-8 buffers) to the outside web world
socket.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    # once max receive data: 1KB
    d = socket.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
# element in list is ByteType
data = b''.join(buffer)
data = data.decode()
# the request header and the request content is split by '\r\n\r\n'
header, html = data.split('\r\n\r\n')

print(header)
print("The html page will be written down in the file called 'sina.html'")
with  open('sina.html', 'w') as f:
    f.write(html)
print('file write finished')
