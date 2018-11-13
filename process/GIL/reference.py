'''example
the reference count for the empty list object[] is 3.
The list object is referenced by a, b, and the argument
passed to sys.getrefcount()
'''
import sys
a = []
b = a
print(sys.getrefcount(a))
