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
def enroll(name, gender, age=5, city='beijing'):
    # ...
    pass

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

# variadic function accepts 0+ parameters, these variable parameters will be auto-stored in a tuple
def calc0(numbers):
    total = 0
    for each in numbers:
#        total  = total + n * n
        pass
    return total

# it is how you call/invoke it
calc0((1, 2, 3, 4, 5))
# only if you use variable function you can invoke the function like that
# calc0(1, 2, 3, 4, 5)

# however you can modify your parameter list as below
def calc1(*numbers):
    total = 0
    for each in numbers:
#        total = total + n * n
        pass
    return total

# the * before parameter list indicate that the parameter will be auto-stored in a tuple
# here you call it
calc1(1, 2, 3, 4)
calc1()

# in this case, what if you have already get a list/tuple ?
numbers = [1, 2, 3, 4, 5]
calc1(numbers[1], numbers[2], numbers[3], numbers[4], numbers[0])
# little mess, right?
# of course there is a simple way as below
calc1(*numbers) # it is very common to see this form


# pure keyword arguments
# you can define a function that takes parameters by name -- and you dont't even have to specify what those names are.
# these are pure keyword function and cannot be passed functionally.
# it will be auto-stored in a dictionary in the somewhere main memory -_-

# the pure arguments fuction
def enroll(name, age, **kwarg):
    # ...
    pass

# how-to-call-it
kwargs = {'city': 'Beijing', 'job': 'Enginerr'}
enroll('Jesse', 20, city=kwargs['city'], job=kwargs['job'])

# or you can simply call it:
enroll('Jesse', 20, **kwargs)

## in summary, you may/can use all these four types of arguments in one function
# a, b is the normal argument, c is the default argument, args is the variadic arguments
# and kwargs is the keyword arugments
def func(a, b, c=0, *args, **kwargs):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kwargs =', kwargs

# example
func(1, 2)
func(1, 2, c=3)
func(1, 2, 'a', 'b', True, )
func(1, 2, 'a', 'b', True, x=99)
## by the last two examples, c , the default argument is assigned automatically and positionally


## recursive function
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

# and another recursive function
def fact(n):
    return fact_iter(n, 1)

# clearly the second function only returns the pure recursive part itself while computing
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

## There is always a possibility to get a traceback as stack over flow,
## but there are always enhancements can made to prevent the case.
print 'https://en.wikipedia.org/wiki/Tail_call'
