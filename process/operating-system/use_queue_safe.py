'''Queue in multithreading
Queue, FifoQueue, PriorityQueue:
Queue is already implemented with thread-safe primitive.
Just use it is absolutely okey.
'''
from queue import Queue, LifoQueue, PriorityQueue
from threading import Thread
import time

products = Queue()

class Producer(Thread):
    def run(self):
        global products
        count = 0
        while True:
            if products.qsize() >= 3:
                pass
            else:
                products.put('new - ' + str(count))
                # print(self.name, 'produces new -', str(count))
                count += 1
            time.sleep(0.5)

class Consumer(Thread):
    global products
    def run(self):
        while True:
            if products.qsize() < 1:
                pass
            else:
                print(self.name, 'bought', products.get())
            time.sleep(1)


def test():
    for i in range(5):
        products.put('old - ' + str(i))

    Producer().start()

    Consumer().start()
    Consumer().start()
    Consumer().start()


if __name__ == '__main__':
    test()

