#!//usr/bin/python

names = ['jesse', 'credit']

print 'call function len()'
print len(names)

print 'call fuction pop()'
names.pop()

print 'call function append()'
names.append('helloworld')

# list insert element
#names.insert(index, 'element')


print 'print list names'
print names
print 'you can update element by assign value directly to its index'

#
print 'the varaible type of each element can be different'

# list contains list

inner = ['This', 'is', 'a', 'list']
names.append(inner)
print 'One list can contains another list'
print names
