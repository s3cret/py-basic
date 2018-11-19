'''When using dict,
if the key you call is not exist,
then it will raise KeyError.
In this case you can use deafultdict to
return your default value.
'''

from collections import defaultdict
# the argument you give to the defaultdict's constructor is a 
# function( could be a lambda ) whose return value type is string

# dd = defaultdict(lambda: 'N/A')
dd = defaultdict(lambda: 'TheDefaultValue')
dd['key1'] = 'abc'
print("dd['key1']", dd['key1'])
print("dd['key100']", dd['key100'])

