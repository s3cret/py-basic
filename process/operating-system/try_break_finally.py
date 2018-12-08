import time
import queue
import random

if __name__ == '__main__':
    while True:
        try:
            r = random.random()
            print('Sleep %.2f second.' % r)
            time.sleep(r)
            if queue.time() > 3:
                print('I will break!')
                break
        finally:
            print('I am finally here!')

