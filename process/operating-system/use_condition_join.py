from threading import Condition, Thread
import time

con = Condition()
count = 100

class Producer(Thread):

    def run(self):
        global count
        while True:
            print(self.name, 'acquiring lock')
            if con.acquire():
                print(self.name, 'acquired lock')
                if count >= 100:
                    print(self.name, 'wait')
                    con.wait()
                else:
                    count = count + 10
                    print(self.name, 'produces 10 just now.',
                            '- remain', str(count))
                    con.notify()
                    con.release()
                    print(self.name, 'released the lock')
                # what if release() like this indent?
                time.sleep(0.1)


class Consumer(Thread):
    def run(self):
        global count
        buy = 10
        while True:
            if con.acquire():
                if count >= buy:
                    count -= buy
                    print(self.name, 'just bought %s' % str(buy),
                            '- remain', str(count))
                    # Is it necessary for cusumer to notify?
                    con.notify()
                    con.release()
                    print(self.name, 'release the lock')
                    print(self.name, 'left.')
                    break

                con.wait()
                print(self.name, 'is waitng')


def test():
    p = Producer(name='Producer', daemon=False)
    p.start()
    # t = Consumer().start()
    c1 = Consumer(name='jesse')
    c1.start()
    c2 = Consumer(name='s3cret')
    c2.start()
    # c3 = Consumer(name='David')
    # c3.start()
    c1.join()
    c2.join()
    # c3.join()

if __name__ == '__main__':
    test()















