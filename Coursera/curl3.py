import os
import urllib.request, urllib.parse, urllib.error

print('Please enter a URL like http://data.pr4e.org/cover3.jpg')
urlstr = input().strip()
if len(urlstr) < 5:
    print('Using default url')
    urlstr = 'http://data.pr4e.org/cover3.jpg'

img = urllib.request.urlopen(urlstr)

# Get the last "word" of the url as filename
words = urlstr.split('/')
fname = words[-1]

# Don't overwrite the file
if os.path.exists(fname):
    if input('Replace ' + fname + ' (Y/n)?') != 'Y':
        print('Data not copied')
        exit()
    print('Replacing', fname)

fhand = open(fname, 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

#print(size, 'characters copied to', fname)
# size is the number of characters downloaded
# one character is 1 Byte (8 bit) already
# transfer it to KB
size = size/1024
print('%.2f KB copied to' % size, fname)
fhand.close()
