'''Bug Fixed, see line 34'''
from threading import Condition, Thread
import time

con = Condition()
count = 100

class Producer(Thread):
    def run(self):
        global count
        while True:
            # let the productory workers get up
            time.sleep(0.1)
            try:
                if con.acquire():
                    if count >= 100:
                        con.wait()
                    else:
                        count = count + 10
                        print(self.name, 'produces 10 just now.',
                                '- remain', str(count))
                        con.notify()
                    # what if release() like this indent?
            finally:
                con.release()


class Consumer(Thread):
    def run(self):
        global count
        buy = 100
        while True:
            try:
                # [bug fixed]
                # it is here you first get the lock
                # and you only release it in else block
                # so it can re-acquire it 10 times
                # [use try ... finally block next time]
                if con.acquire():
                    if count < buy:
                        con.wait()
                    else:
                        count -= buy
                        print(self.name, 'just bought', str(buy), 'and left',
                                'remain -', str(count))
                        con.notify()
                        break
            finally:
                con.release()



if __name__ == '__main__':
    p = Producer(name='Producer', daemon=False)
    p.start()
    # t = Consumer().start()
    c1 = Consumer(name='jesse')
    c1.start()
    c2 = Consumer(name='s3cret')
    c2.start()
    # c3 = Consumer(name='David')
    # c3.start()
    # c1.join()
    # c2.join()
    # c3.join()
















