'''Write your own customize Thread class
Use the parent init method,
and then pass your customized argument.
'''
from threading import Thread, Lock
import time

mutex = Lock()

class ThreadA(Thread):
    def __init__(self, name='default', whatever='default'):
        # Is this two line do the same things?
        # Thread.__init__(self)
        super().__init__()
        self.name = name
        self.whatever = whatever

    def info(self):
        print('My name is', self.name)
        print('Gotya! Stopped thread -', self.whatever)

    def run(self):
        t.join()
        self.info()

def threadingB():
    print("It's time for the guest to get hair cut.")
    time.sleep(0.5)
    print("All hair've cut.")

if __name__ == '__main__':
    t = Thread(target=threadingB, name='jesse')
    t.start()
    ThreadA(whatever=t).start()












