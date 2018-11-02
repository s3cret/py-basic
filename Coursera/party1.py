stuff = list()
stuff.append('python')
stuff.append('chuck')
# this sort do some magic things for the stuff list
stuff.sort()

#print(stuff)
# all the three sentence does exactly the same thing
print (stuff[0]) # this will get the sorted `chunck`
print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))
