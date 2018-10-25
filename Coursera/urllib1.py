import urllib.request
# create url file handle
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    # decode the outside world utf-8 to
    # python inside world unicode
    print(line.decode().strip())
