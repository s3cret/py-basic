numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
# call the built-in function sum and len to the list
average = sum(numlist) / len(numlist)
print('Average:', average)
