'''Global Interpreter Lock
Before executing any python thread, it must acquire the
GIL(Global Interpreter Lock) and then, after executing
100 bytecodes, the interpreter would release the GIL,
giving executable chance to other threads.

It's a historical problem.
Usually we use the official interpreter CPython.
To truely create a molti-core program, there is no way
unless you rewrite an interpreter with no GIL.
Or by writing a multi-process program.
Not too bad, uh-huh?
'''
import threading

def task():
    x = 0
    while True:
        x = x ^ 1

t = threading.Thread(target=task)
t.start()
r = threading.Thread(target=task)
r.start()
