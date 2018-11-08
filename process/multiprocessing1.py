'''multiprocessing1 doc
os.fork() will copy the current process
using which to create a child process
1> in parent process os.fork() returns the child process id
2> in the forked child process os.fork() returns 0
   in this case, child process can retrieve parent process id
   by calling os.getppid() function
'''
import os

if __name__ == '__main__':
    pid = os.fork()
    print('Process %s start ...' % os.getpid())
    if pid == 0:
        print('I am child process %s and my parent process is %s' % (os.getpid(), os.getppid()))
    else:
        print('I am the parent process %s and I have just created %s' % (os.getpid(), pid))
