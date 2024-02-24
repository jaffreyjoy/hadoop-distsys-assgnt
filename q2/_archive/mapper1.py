#!/usr/bin/env python3
"""mapper1.py"""

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    print(line)