from threading import Thread, Lock

class Deadlock(Thread):
    def do1(self):
        global resa, resb
        if mutexA.acquire():
            print(self.name, 'got resa')

            if mutexB.acquire():
                print(self.name, 'got resb')
                mutexB.release()

            mutexA.release()
    def do2(self):
        global resa, resb
        if mutexB.acquire():
            print(self.name, 'got resb')

            if mutexA.acquire():
                print(self.name, 'got resa')

    def run(self):
        self.do1()
        self.do2()

resa = 0
resb = 0
mutexA = Lock()
mutexB = Lock()

def test():
    for i in range(5):
        Deadlock().start()

if __name__ == '__main__':
    test()

