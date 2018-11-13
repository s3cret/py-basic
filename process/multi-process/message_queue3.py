'''Use Queue for example
Create two process in parent process,
one write data to Queue,
another one read data from Queue.
But this time, not terminate the read process.
What if I just leave the read process keep running?
'''
from multiprocessing import Process, Queue
import sys
import os, time, random

# write to queue process
def write(q):
    for value in ['a', 'b', 'c']:
        print('Put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())

# read to queue process
def read(q):
    while True:
        value = q.get(True)
        print('Get %s from queue' % value)

if __name__ == '__main__':
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
    # what if I don't terminate the read process
    # pr.terminate()
    while True:
        i = input('To keep the parent process remaining.\n')
        if i == 'quit':
            pr.terminate()
            break

# finally you will get just two python process of this file
# one is the main parent process
# anther one is the read process waiting to read data from queue
