import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter localtion: ')
    if len(address) < 1: break

    # add parameter address to the url
    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    # open url handle of url file
    urlhandle = urllib.request.urlopen(url)
    # read the whole bunch of file in
    data = urlhandle.read()
    print('Retrieved', len(data), 'characters')
    # decode the outside world utf-8 characters
    # to the python world unicode
    print(data.decode())
    # create the tree structure using
    # xml.etree.ElementTreea.fromstring()
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text
    
    print('lat', lat, 'lng', lng)
    print(location)
