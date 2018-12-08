'''When call con.notify()
the thread will just continue the last wait() line.
'''
from threading import Condition, Thread

con = Condition()
count = 0

class wait_notify(Thread):
    def run(self):
        global count
        while True:
            if con.acquire():
                print(self.name, 'acquired the lock')
                if count < 50:
                    print(self.name, 'is going to con.wait()')
                    con.wait()
                print('I want to wait again!')
                print(con)
                con.wait()
                print('Again I am wake up!')

if __name__ == '__main__':
    w = wait_notify()
    w.start()
