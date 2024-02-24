#!/usr/bin/env python3
"""reducer0.py"""

import sys


prev_person = None
friends = set()

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    curr_person, friend = line.split('\t', 1)

    if curr_person == prev_person:
        friends.add(friend)
    else:
        if prev_person and len(friends)>1:
            # write result to STDOUT
            mutual = prev_person
            for f1 in friends:
                for f2 in friends:
                    if(f1 != f2 and int(f1)<int(f2)):
                        print('%s %s\t%s' % (f1, f2, mutual))
        prev_person = curr_person
        friends = set([friend])


if prev_person and len(friends)>1:
    # write result to STDOUT
    mutual = prev_person
    for f1 in friends:
        for f2 in friends:
            if(f1 != f2 and int(f1)<int(f2)):
                print('%s %s\t%s' % (f1, f2, mutual))