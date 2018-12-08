'''Thread(target=method_or_function).start()'''
from threading import Condition, Thread

con = Condition()
count = 0

def func(name):
    global count
    while True:
        if con.acquire():
            if count < 10:
                print(name, 'is going to wait.')
                print(con)
                con.wait()
                print(name, 'got notified!')
            else:
                # here I only release the lock in the else block
                print('do some stuff and release the lock')
                con.notify()
                '''
                [bug here]
                Each time you will acquire a lock
                when calling con.acquire().
                But you just don't release the rlock unless count >= 10
                [Fix]
                Use try ... finally block properly.
                '''
                con.release()
                break

def tiny():
    ''' if count != 19, it will wait()'''
    while True:
        print(count)
        if con.acquire():
            if count != 19:
                con.wait()
            else:
                print('tiny knows count = 19 now')
                break
    con.release()


if __name__ == '__main__':
    t = Thread(target=func, args=('jesse',))
    t.start()
    i = Thread(target=tiny)
    i.start()
