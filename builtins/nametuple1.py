'''collections.namedtuple
You don't need to write a Point class code block
if you use the collections.namedtuple.
The collections.namedtuple's __doc__ explains
how to deal with module namedtuple
'''
from collections import namedtuple
doc = namedtuple.__doc__
# print(doc)
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('p.x is', p.x)
print('p.y is', p.y)

# also class Point you have just created
# is subclass of tuple
print('ininstance(p, Point)', isinstance(p, Point))
print('ininstance(p, tuple)', isinstance(p, tuple))
