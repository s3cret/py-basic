import time
import sys
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

# inherit from BaseManager
# just to customize the class name
class QueueManager(BaseManager):
    pass

# the QueueManager only retrieve queue from internet,
# so provide with service name is fine when registering
QueueManager.register('get_task_queue')
QueueManager.register('get_receive_queue')
host = ('127.0.0.1', 9999)
# init manager with infomations:
# host and authentication key value
manager = QueueManager(address=host, authkey='abc'.encode())
manager.connect()
# retrieve instances of Queue from manager (instance of QueueManager)
# which means that 
# the two processes share the two queues through the internet
tasks = manager.get_task_queue()
receives = manager.get_receive_queue()

# performing the task from remote host
# send the result back
for i in range(3):
    try:
        # get data from task queue, timeout is one second
        n = tasks.get(timeout=1)
        # show doing tasks
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        # send the task result to the receive queue to remote host
        receives.put(r)
    except Exception as e:
        print(e)

# this worker process don't control the QueueManager
# just do nothing with it will be fine
print('worker exit')
