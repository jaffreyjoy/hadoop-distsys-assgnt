#!/usr/bin/env python3
"""mapper0.py"""

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    f1, f2 = line.split(' ', 1)
    # if(int(f1)<int(f2)):
    #     print('%s\t%s' % (f1, f2))
    # else:
    #     print('%s\t%s' % (f2, f1))
    print('%s\t%s' % (f1, f2))
    print('%s\t%s' % (f2, f1))
