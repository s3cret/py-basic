'''To create threads local variables
The usually usage of ThreadLocal is, for example, binding a database
to a thread, or binding http-request to a thread handling a user's
authentication.
'''
import threading
import time, random

local_school = threading.local()

def task1_1():
    print('I am %s from %s' % (local_school.name, threading.currentThread().name))
    time.sleep(random.random())
    print('Again, I am %s from %s' % (local_school.name, threading.currentThread().name))

def thread1_do():
    # do nothing but create a subcall calling task1()
    task1_1()

def task2_1():
    print('I am %s from %s' % (local_school.name, threading.currentThread().name))
    time.sleep(random.random())
    print('Again, I am %s from %s' % (local_school.name, threading.currentThread().name))

def thread2_do():
    # do nothing but create a subcall calling task1()
    task2_1()

# thread1 do a lot of works
# including task1_1, task1_2
def thread1(name):
    local_school.name = name
    thread1_do()

def thread2(name):
    local_school.name = name
    thread2_do()

if __name__ == '__main__':
    t1 = threading.Thread(target=thread1, args=('jesse',), name='Thread-A')
    t2 = threading.Thread(target=thread1, args=('s3cret',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
