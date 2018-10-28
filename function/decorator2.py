import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Call', func.__name__)
        return func(*args, **kwargs)
    print('End', func.__name__)
    return wrapper

@log
def myfunc():
    print('This is my func:', myfunc.__name__)

myfunc()
