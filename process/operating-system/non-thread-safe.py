from threading import Thread
import time

class Mythread(Thread):
    def run(self):
        global num
        time.sleep(0.1)
        num = num + 1
        print(self.name, "set num to", str(num))

num = 0
def test():
    for i in range(5):
        t = Mythread()
        t.start()

if __name__ == '__main__':
    test()

