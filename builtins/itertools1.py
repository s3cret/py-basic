import itertools
# one infinite loop:
def itertools_count():
    '''this func will not stop unless you press Ctrl+C'''
    natuals  = itertools.count(1)
    for n in natuals:
        print(n)

# cycle(), you can see it from its name
def itertools_cycle():
    '''this func will not stop unless you press Ctrl+C'''
    c = itertools.cycle('ABCABC')
    for each in c:
        print(each)

# repeat(), a nice version of cycle
# whose second argument is count to repeat
def itertools_repeat():
    '''nice version of cycle'''
    r = itertools.repeat('abc', 10)
    for each in r:
        print(each)

# for infinite loops, function takewhile() will
# porvide with a condition judgement to decide
# when to break a loop
def itertools_takewhile():
    '''the loop will end according to the lambda()
passed in the constructor of itertools.takewhile()'''
    c = itertools.count(1)
    tkw = itertools.takewhile(lambda x: x <= 10, c)
    for each in tkw:
        print(each)

