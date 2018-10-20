#!/usr/bin/python
## 'return' None equals 'return'

## reserve word 'pass' use for place holder to make sure some part can run
def nop():
    pass

## return multiple values
# as a matter of fact, it just return a tuple type value to implement multiple.

# ...

## parameters
# the default parameter should be the last one
def enroll(name, gender, age=5 city='beijing'):
# ...
# ...
# ...

# what is the difference between the two functions below ?

def add_end(L=[]):
    L.append('END')
    return L


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# you don't need to lock the second function

# give a list/tuple
def calc0(numbers):
    total = 0
    for each in numbers:
        total  = total + n * n
    return total

# it is how you call/invoke it
calc0((1, 2, 3, 4, 5))
# or
calc0(1, 2, 3, 4, 5)

# however you can modify your parameter list as below
def calc1(*numbers):
    total = 0
    for each in numbers:
        total = total + n * n
    return total

# the * before parameter list indicate that the parameter will be auto-stored in a tuple
# here you call it
calc1(1, 2, 3, 4)
calc1()

# in this case, what if you have already get a list/tuple ?
numbers = [1, 2, 3, 4, 5]
calc1(numbers[1], numbers[2], numbers[3], numbers[4], numbers[5])
# little mess, right?
# of course there is a simple way as below
cal1(*numbers) # it is very common to see this form

