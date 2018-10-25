# Actually it is no need to import urllib.error, urllib.parse
# unless you really need it
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# maybe you should promote a decode()
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG itself:', tag)
    print('URL tag attr href, default None:', tag.get('href', None))
    # the a tag contends
    print('Contents:', tag.contents[0])
    # all the tag's attributes
    print('Attrs:', tag.attrs)
