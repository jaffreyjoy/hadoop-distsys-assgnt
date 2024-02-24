#!/usr/bin/env python3
"""mapper0.py"""

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if(line.count('\t') != 0):
        node, adjlist = line.split('\t', 1)
        adjlist = adjlist.split(' ')
        node_dist_pairs = []
        # add its own node dist pair
        print("%s\t%s %s" % (node, node, 0))
        # add its adj dist pairs with dist 1
        for adjnode in adjlist:
            print("%s\t%s %s" % (node, adjnode, 1))
            print("%s\t%s %s" % (adjnode, node, 1))
            # node_dist_pairs.append([adjnode, 1])
        # add cross adj pairs with dist 2
        for ladj in adjlist:
            for radj in adjlist:
                if(ladj != radj):
                    print("%s\t%s %s" % (ladj, radj, 2))
    else:
        if (line != ''):
            node = line
            print("%s\t%s %s" % (node, node, 0))