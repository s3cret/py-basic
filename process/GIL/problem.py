'''Back to the GIL
The problem is that this reference count variable needed protection
from race conditions where two threads increase or decrease its value
simultaneously.
If this happens, it can cause either leaked memory that is never
relesed or, even worse, incorrectly release the memory while a
reference to that object still exists, which causes crashes or other
weird bugs in your Python programs.
'''
