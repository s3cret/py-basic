'''deque, effective two-way list for insertion and deletion
mostly used in queue and stack.
It is very effective to insert or delete the header element.
'''
from collections import deque
import os
d = deque([x for x in os.listdir()])

# perform some append
# append func is also known as appendright
d.append('append')
d.appendleft('appendleft')
print(d)

# perform some pop
d.pop()
print(d)
d.popleft()
print(d)

