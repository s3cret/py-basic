# Search for lines that start with From and have an at sign
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # call re.search(regular_expression, from_which_string)
    # ^ starts, . stands for any characters except \r, \n,
    # + stands for the re in front of it appears 1 or any times
    if re.search('^From:.+@', line):
        print(line)
