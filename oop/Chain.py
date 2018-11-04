class Chain(object):
    def __init__(self, path=''):
        #print("init", path)
        self.path = path

    # when instance__getattr__(path) is called, return a
    # class(instance.path/path)
    def __getattr__(self, attr):
        #print('get', attr)
        return Chain('%s/%s' % (self.path, attr))

    def __str__(self):
        return self.path
    #__repr__ = __str__

    # when instance('attr') is called, return a class(instance.self.path/attr)
    # very similar to __getattr__
    def __call__(self, attr):
        return Chain('%s/%s' % (self.path, attr))
