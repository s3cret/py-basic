# Search for lines that start with 'F', followed by
# any 2 characters, followed by 'm:'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # call re.search(regular_expression, from_which_sentence)
    # ^ stands for re starts, . stands for any character except \n, \r
    if re.search('^F..m:', line):
        print(line)
