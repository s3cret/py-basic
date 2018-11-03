# Search for lines that start with From and have an at sign
import re
hand = open('mbox.txt')
rex = input('Enter a regular expression: ')
count = 0
results = list()
for line in hand:
    line = line.rstrip()
    if re.search(rex, line):
        count = count + 1
        results.append(line)

print('mbox.txt had', count, 'lines that matched', rex)
print()
printout = input('Check them out? (y/n)\n')
if printout == 'y':
    for each in results:
        print(each)
