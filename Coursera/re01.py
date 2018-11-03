# Search for lines that contain 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # call re.search(regular_expression, from_which_sentence)
    if re.search('From:', line):
        print(line)
