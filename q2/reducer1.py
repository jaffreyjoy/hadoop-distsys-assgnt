#!/usr/bin/env python3
"""reducer1.py"""

import sys


prev_person_pair = None
mutuals = set()

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    curr_person_pair, mutual = line.split('\t', 1)

    if prev_person_pair==curr_person_pair:
        mutuals.add(int(mutual))
    else:
        if prev_person_pair:
            print('%s\t%s' % (prev_person_pair, " ".join([str(el) for el in sorted(list(  mutuals  ))])))
        prev_person_pair = curr_person_pair
        mutuals = set([int(mutual)])
if prev_person_pair:
    print('%s\t%s' % (prev_person_pair, " ".join([str(el) for el in sorted(list(  mutuals  ))])))