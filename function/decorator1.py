def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            wrapper.__name__ = func.__name__
            return func(*args, **kw)
        return wrapper
    return decorator

@log('call')
def out():
    print('here is the function')
    print('out function name:', out.__name__)

out()
