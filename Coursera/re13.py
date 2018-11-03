# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
import re
hand = open('mbox-short.txt')
i = 0
for line in hand:
    line = line.rstrip()
    # retieve the time string
    #x = re.findall('^From .*([0-9]{2}:[0-9]{2}:[0-9]{2})', line)
    #x = re.findall('^From (.*)?', line)
    x = re.findall('^From .*?([0-9][0-9]:)', line)
    if len(x) > 0:
        print(line)
        print(x)
