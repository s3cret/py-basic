'''What about the programs where some threads are I/O-bound
and some are CPU-bound?
In such programs, Python's GIL was known to starve the I/O-bound
threads by not giving them a chance to acquire the GIL from
CPU-bound threads.
This is because of a mechanism built into Python that forces
threads to release the GIL after a fixed interval of continuous
use and if nobody else acquire the GIL, the same thread could
continue its use.
'''

import sys
# the interval is set to 100 instructions:
# DeprecationgWarning: sys.getcheckinterval() and
# sys.setcheckinterval() are depreacted.
# Use sys.checkswitchinterval() instead.
i = sys.getcheckinterval()
# what's this line doing?
#i = sys.getswitchinterval()
print(i)
