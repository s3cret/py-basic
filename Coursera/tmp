import urllib.request
import ssl

# ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.baidu.com'
html = urllib.request.urlopen(url, context=ctx).read()

print(html.decode())
