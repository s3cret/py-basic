'''Difference between run() and start():
If you invoke run() directly, it's executed on the calling thread,
just like any other method call.
When you call Thread.start(), it starts a new thread,
and calls the run() method of the runnable instance internally
to execute it within that thread.
'''
import time, threading, random

def task():
    current_thread_name = threading.currentThread().name
    print('Thread %s is running ...' % current_thread_name)

    for i in range(5):
        print('Thread %s is working on task %s' % (current_thread_name, i))
        time.sleep(random.random())

    print('Thread %s is done ...' % current_thread_name)

if __name__ == '__main__':
    current_thread_name = threading.currentThread().name
    print('Thread %s is running ...' % current_thread_name)

    t = threading.Thread(target=task, name="jesse")
    r = threading.Thread(target=task, name="s3cret")

    # If you invoke run() dirctly, it's executing on the current thread,
    # which is 'MainThread' in this case, just like any other method call.
    #t.run()

    # here comes the method start()
    t.start()
    r.start()

    # running in the main thread, you cannot call join()
    # or it raise RuntimeError
    #t.join()
    r.join()
    print('Thread %s is done ...' % current_thread_name)
