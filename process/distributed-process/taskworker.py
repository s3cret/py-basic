import time
import sys
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

# the QueueManager only retrieve queue from internet,
# so only when registering provide with service name is fine
QueueManager.register('get_task_queue')
QueueManager.register('get_receive_queue')
host = ('127.0.0.1', 9999)
# init manager with infomations:
# host and authentication key value
manager = QueueManager(address=host, authkey='abc'.encode())
manager.connect()
# retrieve instances of Queue
tasks = manager.get_task_queue()
receives = manager.get_receive_queue()
# retrieve from tasks
for i in range(3):
    try:
        n = tasks.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        receives.put(r)
    except Exception as e:
        print(e)

print('worker exit')
