#!/usr/local/bin/python3
# promote a filename
filename = input('Enter a filename:\n')
# create a handle for the input filename
handle = open(filename)

# store the whole bunch words of the file 
count = dict()
for line in handle:
    words = line.strip().split()
    for word in words:
        count[word] = count.get(word, 0) + 1

# you must reverse the dict
# use list comprehension
lis = list()
for k, v in count.items():
    lis.append((v, k))
lis = sorted(lis, reverse=True)

for k, v in lis[:10]:
    #print(k, v)
    pass

# I encourage you to understand every single line of this code

# all that from 12 to 18 lines can be a even simple version using list comprehension within one line as follow
# as a matter of fact, it is not one line, just a little simple

# 1. using list comprehension to generate the list
# 2. using the high-order function sorted() with reverse option equals True
simple_list = sorted([ (v, k) for k, v in count.items() ], reverse=True)
#print(simple_list[:10])
# still, it is not the same as before
for k, v in simple_list[:10]:
    print(k, v)

