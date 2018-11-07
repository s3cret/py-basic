from multiprocessing import Process
import os
import time

def run_proc(name):
    begin = time.time()
    print('Run child process %s (%s) ...' % (name, os.getpid()))
    time.sleep(2)
    end = time.time()
    print('Child process done, used %.2f seconds' % (end - begin))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    # init two Process()
    # actually these can be a Pool Object with which to handle
    p = Process(target=run_proc, args=('test',))
    q = Process(target=run_proc, args=('jesse',))
    print('process will start ---')
    # Process.start() will start the instance of Process
    p.start()
    q.start()
    # Process.join() will wait till the child process is finished
    #p.join()
    #q.join()
    # this will wait all the child process done before print()
    print('all child process end # this line is under p.join()')
