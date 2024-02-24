#!/usr/bin/env python3
"""mapper2.py"""

import sys


for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    print(line)