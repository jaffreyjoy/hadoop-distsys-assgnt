#!/usr/bin/env python3
"""reducer1.py"""

import sys


prev_friend_pair = None
prev_mutuals = set()

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    curr_friend_pair, mutuals = line.split('\t', 1)
    mutuals = set([int(el) for el in mutuals.split(' ')])

    if prev_friend_pair==curr_friend_pair:
        common = mutuals.intersection(prev_mutuals)
        if(len(common)>0):
            print('%s\t%s' % (prev_friend_pair, " ".join([str(el) for el in sorted(list(  common  ))])))
        prev_friend_pair = None
        prev_mutuals = set()
    else:
        prev_friend_pair = curr_friend_pair
        prev_mutuals = mutuals