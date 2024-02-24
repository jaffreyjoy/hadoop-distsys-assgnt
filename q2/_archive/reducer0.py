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
            for friend in friends:
                mutuals = []
                for mutual in friends:
                    if(friend != mutual):
                        mutuals.append(mutual)
                if(int(friend)>int(prev_person)):
                    print('%s %s\t%s' % (prev_person, friend, " ".join(mutuals)))
                else:
                    print('%s %s\t%s' % (friend, prev_person, " ".join(mutuals)))
        friends = set([friend])
        prev_person = curr_person


if prev_person and len(friends)>1:
    # write result to STDOUT
    for friend in friends:
        mutuals = []
        for mutual in friends:
            if(friend != mutual):
                mutuals.append(mutual)
        if(int(friend)>int(prev_person)):
            print('%s %s\t%s' % (prev_person, friend, " ".join(mutuals)))
        else:
            print('%s %s\t%s' % (friend, prev_person, " ".join(mutuals)))