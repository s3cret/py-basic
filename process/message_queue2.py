'''Use Queue for example
Create two process in parent process,
one write data to Queue,
another one read data from Queue.
This time let the read process terminate itself
after it receives three data.
'''
from multiprocessing import Process, Queue
import os, time, random

# write to queue process
def write(q):
    for value in ['a', 'b', 'c']:
        print('Put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())

# read to queue process
def read(q):
    _count = 0
    while True:
        value = q.get(True)
        if len(value) > 0:
            _count += 1
            print('Get %s from queue' % value)
        if _count == 3:
            print('Read process done with 3 words.')
            break

if __name__ == '__main__':
    print(__doc__)
    # init a Queue instance
    q = Queue()
    # init the write process
    pw = Process(target=write, args=(q,))
    # init the read process
    pr = Process(target=read, args=(q,))
    # start the write process
    # the write process will terminate after all jobs done
    pw.start()
    # start read process
    # the read process will not terminate
    # because it's a infinity loop waiting for data from queue
    pr.start()
    # wait the write process done
    pw.join()
    # and then terminate the read process
    # already terminated
    # pr.terminate()

