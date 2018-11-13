import random
import time
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

# send task queue
task_queue = Queue()

# receive task queue
rece_queue = Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_receive_queue', callable=lambda: rece_queue)
# bind to localhost:9999, authentication key value is 'abc'
manager = QueueManager(address=('', 9999), authkey='abc'.encode())
manager.start()
# retrieve Queue instances through networking
tasks = manager.get_task_queue()
receive = manager.get_receive_queue()

for i in range(3):
    n = random.randint(0, 1000)
    print('Put task %d' % n)
    tasks.put(n)

for i in range(3):
    r = receive.get(timeout=10)
    print('Receive: %s' % r)

print('manager exit')
manager.shutdown()

