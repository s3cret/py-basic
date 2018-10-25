import json
# store the json-formatted in a list
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''
# using json.loads()
info = json.loads(data)
print('User count:', len(info))
# item is the info[0], info[1]
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
    # print \n
    print()
