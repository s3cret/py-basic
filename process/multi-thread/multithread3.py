'''multi-thread access(modify/operate) with one variable'''

import threading
import time

ticket = 1

def buy(name):
    print(name, 'is going to buy a ticket.')
    global ticket
    if ticket > 0:
        time.sleep(1)
        ticket -= 1
        print(name, 'just bought the last ticket.')
    else:
        print('Tickets have already sold out.')

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
