fhandle = open('mbox-short.txt')
count = 0
for line in fhandle:
    count = count + 1
print('Line Count:', count)
