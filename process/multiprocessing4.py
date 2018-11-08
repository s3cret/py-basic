from multiprocessing import Pool
import os
import time

def task(name):
    begin = time.time()
    print('Task %s (%s) is starting ...' % (name, os.getpid()))
    time.sleep(2)
    end = time.time()
    print('Task %s (%s) is done ...' % (name, os.getpid()))

#if __name__ == '__main__':
def main()
    begin = time.time()
    print('Main process (%s) start' % os.getpid())
    # You can specify the number of process running during the same time
    # by set option processes=number
    pool = Pool(1)
    for i in range(9):
        pool.apply_async(task, args=(i,))
    pool.close()
    pool.join()
    end = time.time()
    print('All job done in %.3f seconds' % (end - begin))

