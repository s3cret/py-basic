import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
# print(img) # never execute this line, it is not good at all
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()
