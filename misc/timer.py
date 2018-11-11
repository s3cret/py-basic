from multiprocessing import Process, Pool
import time

class DecoratorTimer():

    def __init__(self, func):
        self.func = func
        self.precise = 3

    def __call__(self, *args, **kwargs):
        print(('--- All jobs start --- (%.' + str(self.precise) + 'fs)') % (0))
        start = time.time()
        self.func(*args, **kwargs)
        end = time.time()
        print(('--- All jobs done  --- (%.' + str(self.precise) + 'fs)') % (end - start))

    # just layout here
#    def __call__(self, *args, **kwargs):
#        print('begin')
#        self.func(*args, **kwargs)
#        print('end')

# this one kind of sucks
class Functimer():

    def __init__(self, *func, precise=3, processes=None):
        self.precise = precise
        self.func = func
        self.processes = processes

    def run(self):
        if len(self.func) == 1:
            self.__run_process()
        elif len(self.func) > 1:
            self.__run_pool()

    def __run_process(self):
        print(('--- All jobs start --- (%.' + str(self.precise) + 'fs)') % (0))
        start = time.time()
        process = Process(target=self.func[0])
        process.start()
        process.join()
        end = time.time()
        print(('--- All jobs done  --- (%.' + str(self.precise) + 'fs)') % (end - start))

    def __run_pool(self):
        '''This func wastes too much time in creating Pool object'''
        print(('--- All jobs start --- (%.' + str(self.precise) + 'fs)') % (0))
        start = time.time()
        pool = Pool()
        for each in self.func:
            pool.apply(each)
        pool.close()
        pool.join()
        end = time.time()
        end = end - 0.10873
        print(('--- All jobs done  --- (%.' + str(self.precise) + 'fs)') % (end - start))

# this is just an example
def log(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print('start', start)
        return func(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    @DecoratorTimer
    def test():
        print('this is test')

    test()

    # functimer = Functimer(test, test, test, test)
    # functimer.run()
    # functimer2 = Functimer(test)
    # functimer2.run()
