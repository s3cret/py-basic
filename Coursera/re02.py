# Search for lines that start with 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # call re.search(regular_expression, from_which_sentence)
    # re: ^ stands for a re starts, $, respectively, stands for a re ends
    if re.search('^From:', line):
        print(line)
