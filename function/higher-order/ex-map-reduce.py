#!/usr/local/bin/python3
'''
In python3,
1. map() returns a iterator rather than a list,
use list(map(func, seq)) to get a list
2. reduce() is removed from __builtins__,
you need to import it:
from functools import reduce
'''

# function to captialize the namelist
def capitalize(lst):
    def char2lower(c):
        return c.lower()
    def str2cap(s):
        return s[0].upper() + ''.join(map(char2lower, s[1:]))
    return map(str2cap, lst)

    # actually the code below does the same work as map()
    #def main(lst):
    #    fixed_list = list()
    #    for each in lst:
    #        fixed_list.append(str2cap(each))
    #    return fixed_list
    #return main(lst)

namelist = list()
print('Enter your name:\n(EOF to quit)')
while True:
    name = input()
    if name == "EOF":
        break
    namelist.append(name)
if len(namelist) == 0:
    quit(9)
print('Congratulations!!!')
#print(capitalize(namelist))
print(list(capitalize(namelist)))

