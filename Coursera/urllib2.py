import urllib.request, urllib.parse, urllib.error
# create url file handle
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
