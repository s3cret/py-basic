import xml.etree.ElementTree as ET
# xml data input
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>
'''
# using the xml.etree.ElementTree as ET
# call function fromstring(str)
tree = ET.fromstring(data)
# find('str') and get('str', retnval)
print('Name:', tree.find('name').text)
# format the phone_text
# remove all the blank characters
phone_text = tree.find('phone').text.strip()
#print(type(phone_text))
print(phone_text)
print('Phone Attr type:', tree.find('phone').get('type'))
print('Email Attr hide:', tree.find('email').get('hide'))
print('Email none-exist attr:', tree.find('email').get('did', "none-exist"))
