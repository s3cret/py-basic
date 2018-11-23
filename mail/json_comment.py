'''for now // and /* type of comment is not supported.'''
import json
with open('key.json', 'r') as f:
    content = f.read()
    keys = json.loads(content)
print(keys)

