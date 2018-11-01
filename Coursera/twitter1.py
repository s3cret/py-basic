import urllib
import twurl
import ssl

# https://apps.twitter.com
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore the SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = None
ctx.verify_mode = ssl.CERT_NONE

while True:
    print()
    account = input('Enter Twitter Account - ')
    if (len(account) < 1): break
    url = twurl.augment(TWITTER_URL, {'screen_name': account, 'count': 2})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print(data[:250])

    # get headers
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
