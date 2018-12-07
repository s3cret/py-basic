'''Use Lock and RLock(Reentrant lock)
acquire():
The RLock contains a Lock inside and a counter,
when the second time the lock is acquire()ed,
it will add 1 to the inside counter,
rather than attempt to acquire the lock.

release():
Finally, when the inside counter becomes to 0,
it will release the lock.
Executed code below:
```
if not count:
    self.__owner = None
    self.__block.release()
```

'''
from threading import Lock, Thread, RLock
import time

mutex = Lock()
rmutex = RLock()

class Solved(Thread):
    def run(self):
        rmutex.acquire(1)
        print(self.name, 'acquire the rmutex')
        time.sleep(1)

        print(self.name, 'wating to acquire the rmutex again')
        # the counter will add 1, not attempt to acquire the lock
        # which it already has.
        rmutex.acquire()
        print(self.name, 'succeed in acquiring the rmutex again')
        # do some stuff
        pass
        rmutex.release()
        rmutex.release()

class NotSolved(Thread):
    def run(self):
        mutex.acquire(1)
        print(self.name, 'acquire the mutex')
        time.sleep(1)

        print(self.name, 'wating to acquire the mutex again')
        # it will be blocked for acquiring the second lock
        mutex.acquire()
        # do some stuff
        pass
        mutex.release()
        mutex.release()

def test():
    for i in range(5):
        # NotSolved().start()
        Solved().start()

if __name__ == '__main__':
    test()

