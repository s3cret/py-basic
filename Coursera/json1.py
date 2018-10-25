import json
# json data input
data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''
# actually it parse the json-format file directly
# to the python dictionary
# using json.loads('json-format-strings')
info = json.loads(data)
# visit all the data just as using dict
print('Name:', info["name"])
print('{ email {hide} }:', info["email"]["hide"])
