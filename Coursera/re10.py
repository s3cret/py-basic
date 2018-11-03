# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
import re
hand = open('mbox-short.txt')
rex = '^X\S*: [0-9.]+'
i = 0
for line in hand:
    line = line.rstrip()
    # if re.search(rex, line):
    #     print(line)
    lst = re.findall(rex, line)
    if len(lst) > 0:
        i += 1
        print(lst)
    if i > 5: break
