'''Difference between multi-process and multi-thread
In multi-process, a variable is forked and owned by its
process only.
In multi-thread, a variable is shared with each thread, and
each variable can be changed/modified by each thread.
Thus, the biggest problem in multi-thread is serveral threads
access one variable in the same time messing up the value of
variables.
'''

import time, threading

balance = 0

def change_it(n):
    # first save and then retrieve
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(1000000):
        change_it(n)
    print('thread %s done' % threading.currentThread().name)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)
