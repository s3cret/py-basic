import threading
import time
import random

thread_locals = threading.local()

def task1():
    thread_locals.number = 1
    print('%s start' % threading.currentThread().name)
    while True:
        print('%s I am preforming the computing things.' % thread_locals.number)
        time.sleep(random.random() * 3)

def task2():
    thread_locals.number = 2
    print('%s start' % threading.currentThread().name)
    while True:
        print('%s Gui is running' % thread_locals.number)
        time.sleep(random.random())

gui_thread = threading.Thread(target=task2, name='GUI-thread')
working_thread = threading.Thread(target=task1, name='Working-thread')

working_thread.start()
gui_thread.start()

working_thread.join()
gui_thread.join()

