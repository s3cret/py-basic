from threading import Condition, Thread
import time

con = Condition()
count = 100

class Producer(Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                print(self.name, 'acquired the lock')
                if count >= 100:
                    con.wait()
                    print(self.name, 'wait and give away the lock')
                else:
                    count = count + 50
                    print(self.name, 'produces 10 just now.',
                            'remain', str(count))
                    con.notify()
            con.release()
            print(self.name, 'released the lock')
            time.sleep(0.5)

class Consumer(Thread):
    def run(self):
        global count
        buy = 100
        bought = False
        while True:
            if con.acquire():
                print(self.name, 'acquired the lock')
                if count < buy:
                    con.wait()
                    print(self.name, 'is waitng')
                else:
                    count -= buy
                    bought = True
                    print(self.name, 'just bought %s. and left.' % str(buy),
                            'remain', str(count))
                    con.notify()
            con.release()
            print(self.name, 'release the lock')
            if bought: break


def test():
    for i in range(1):
        Producer(name='Producer', daemon=False).start()

    print('jesse comes into shop')
    Consumer(name='jesse').start()
    print('quicker comes into shop')
    Consumer(name='quicker').start()

if __name__ == '__main__':
    test()















