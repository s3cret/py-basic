import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''
# call xml.etree.ElementTree.fromstring()
stuff = ET.fromstring(input)
# get the nodes user under users
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name Tag-itself', item.find('name'))
    print('Name Attr x:', item.get('x'))
    print('Id', item.find('id').text)
    # print \n to tidy the output
    print()
