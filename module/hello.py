#!/usr/bin/env python

' why this is __doc__ '
' Is this also a part of __doc__ ?'
' No. Only the first line is the __doc__ .'

__author__ = 'jesse s3cret'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

'Will I be appended to __doc__ ?'
'No.'
