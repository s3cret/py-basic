from multiprocessing import Pool
import os, time, random

def task(name):
    print('Task %s (%s) is running ...' % (name, os.getpid()))
    start = time.time()
    #time.sleep(random.random() * 3)
    time.sleep(2)
    # Warning: because you call sleep instead of time() here
    # so the rest of the codes in this function don't run
    end = time.sleep()
    print('What happen to the few lines of the code below?')
    print('Sleep done')
    print('Task %s runs %0.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
    main_start = time.time()
    print('Parent process %s running' % os.getpid())
    pool = Pool(5)
    for i in range(5):
        pool.apply_async(task, args=(i,))
    print('--- all subprocess begin ---')
    # close the pool in order not to add new process to it
    pool.close()
    # must Pool.close() before Pool.join()
    pool.join() # Pool.join() waits for all the subprocess done
    print('--- all subprocess done ---')
    main_end = time.time()
    print('Main process runs %.2f seconds' % (main_end - main_start))
