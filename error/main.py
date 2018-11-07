from error import FooError
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
foo(0)
