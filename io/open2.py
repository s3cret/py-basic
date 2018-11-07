f = open('foo')
# read the whole bunch of file buffer to the main memory
content = f.read()
print('--- Begin ---')
print(content, end='')
print('--- End ---')
f.close()
