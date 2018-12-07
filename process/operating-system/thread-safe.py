from threading import Thread, Lock
import time

mutex = Lock()

class Mythread(Thread):
    def run(self):
        global num
        # when timeout is set, other threads will only
        # wait until timeout and then run no matter whether
        # it acquires the lock or not
        #mutex.acquire(timeout=2)
        mutex.acquire()
        try:
            # time.sleep(0.1)
            num = num + 1
            print(self.name, "set num to", str(num))
        finally:
            mutex.release()
            pass

num = 0
def test():
    for i in range(5):
        t = Mythread()
        t.start()

if __name__ == '__main__':
    test()

