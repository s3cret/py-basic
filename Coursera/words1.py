#!/usr/local/bin/python3
# promote a filename
filename = input('Enter your filename:\n')
# create a handle
handle = open(filename)

# store the whole bunch of file in the dictionary
# actually you can use a list comprehention to 
# generate the list below
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or bigcount < count:
        bigcount = count
        bigword = word

print(bigword, bigcount)
