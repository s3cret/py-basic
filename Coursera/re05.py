import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# \s matches all the blank characters, \S is the opposite
lst = re.findall('\S+@\S+', s)
print(lst)
