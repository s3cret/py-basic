import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# check all the 

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

todo = list()
visited = list()
url = input('Enter - ')
todo.append(url)
count = int(input('How many to retrieve - '))

# `todo` list contains urls to be visited
# `count` is how many the user want to
while len(todo) > 0 and count > 0 :
    # dealing with the last one url in list todo
    url = todo.pop()
    # do some checks

    if (not url.startswith('http')):
        #print("Skipping", url)
        continue

    if (url.find('facebook') > 0):
        continue

    if (url.find('linkedin') > 0):
        continue

    if (url in visited):
        print("Visited", url)
        continue

    print("====== To Retrieve:",count, "Queue Length:", len(todo))
    count = count - 1

    print("===== Retrieving ", url)
    visited.append(url)

    try:
        # using urllib.request.urlopen
        # to create url file handle
        html = urllib.request.urlopen(url, context=ctx).read()
    except:
        print("*** Error in retrieval")
        continue

    # use the BeautifulSoup to parse html
    # 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags from the current url
    # append it to todo list
    tags = soup('a')
    for tag in tags:
        newurl = tag.get('href', None)
        if (newurl is not None):
            # if newurl is not None
            # append it to todo list
            todo.append(newurl)
