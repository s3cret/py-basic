import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
phone_text = tree.find('phone').text.strip()
#print(type(phone_text))
print(phone_text)
print('Phone type:', tree.find('phone').get('type'))
print('Email:', tree.find('email').get('hide'))
print('Email none-exist attr:', tree.find('email').get('did', "none-exist"))
