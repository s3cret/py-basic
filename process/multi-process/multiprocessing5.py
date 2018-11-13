from multiprocessing import Process
import os
import time

def task1(name):
    begin = time.time()
    print('--- task1 process start --- (%s)' % os.getpid())
    time.sleep(1.5)
    end = time.time()
    print('--- task1 process done --- (%.2f seconds)' % (end - begin))

def task2(name):
    begin = time.time()
    print('--- task2 process start --- (%s)' % os.getpid())
    time.sleep(3)
    end = time.time()
    print('--- task2 process done --- (%.2f seconds)' % (end - begin))

# create 2 process
if __name__ == '__main__':
    print('----- Main process start ----- (%s)' % os.getpid())
    p1 = Process(target=task1, args=('jesse',))
    p2 = Process(target=task2, args=('s3cret',))
    print('start all subprocesses')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('----- Main process done  -----')
