# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
# Just a retrieve.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # use () to do a sub retrieve
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
