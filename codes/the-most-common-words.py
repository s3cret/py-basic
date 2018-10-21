#!/usr/local/bin/python3
filename = input('Enter your filename:\n')
handle = open(filename)

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
