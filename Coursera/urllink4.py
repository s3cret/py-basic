import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

todo = list()
visited = list()
url = input('Enter - ')
todo.append(url)
count = int(input('How many to retrieve - '))

while len(todo) > 0 and count > 0:
    print('=== To Retrieve:', count, 'Queue Length:', len(todo))
    url = todo.pop()
    print('>>> Retrieving ' + '\n' + url)
    print()
    count = count - 1

    if (not url.startswith('http')):
        print('Skipping', url)
        continue

    if (url.find('github') > 0):
        continue

    if (url.find('facebook') > 0):
        continue

    if (url in visited):
        print('*** Already visited ', url)
        continue

    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except:
        print('*** Error in retrieval ***')
        continue

    soup = BeautifulSoup(html, 'html.parser')
    visited.append(url)

    # Retrieve all of the anchor tags
    alist = soup('a')
    for tag in alist:
        newurl = tag.get('href', None)
        if (newurl is not None):
            todo.append(newurl)
