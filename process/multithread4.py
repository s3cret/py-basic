'''multi-thread access(modify/operate) with one variable
add lock to prevent case 3 happening
Lock lowers the efficiency of the multi-threads program.
Actually one process can init servral locks,
different thread gets different lock, when they try to
acquire the lock from the other side thread, it may results
into `dead lock`
'''

import threading
import time

ticket = 1
lock = threading.Lock()

def buy(name):
    lock.acquire()
    print(name, 'is going to buy a ticket.')
    global ticket
    try:
        if ticket > 0:
            time.sleep(1)
            ticket -= 1
            print(name, 'just bought the last ticket.')
        else:
            print('Tickets have already sold out.')
    finally:
        # use try ... finally to ensure the lock should be release
        # in case that other threads never get lock to access variable
        lock.release()

if __name__ == '__main__':
    jesse = threading.Thread(target=buy, args=('jesse',), name='jesse_buy_tickets')
    s3cret = threading.Thread(target=buy, args=('s3cret',), name='s3cret_buy_tickets')

    jesse.start()
    s3cret.start()
    jesse.join()
    s3cret.join()

    print('Final ticket num:', ticket)
    if ticket < 0:
        print('Boom! Error! Boom!')

