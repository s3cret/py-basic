import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

# one character is 1 Byte(8 bit) already
# transfer to Byte number
size = size/1024
print(size, 'characters copied.')
print('%.2f KB download' % size)
fhand.close()
