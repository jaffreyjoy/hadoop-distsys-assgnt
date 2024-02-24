#!/usr/bin/env python3
"""mapper1.py"""

import sys


for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    node, rnode_dist_pairs  = line.split('\t', 1)
    rnode_dist_pairs = set([tuple([int(el) for el in  rnode_dist_pair.split(' ')]) for rnode_dist_pair in rnode_dist_pairs.split('\t')])

    print("%s\t%s %s" % (node, node, 0))

    for dest, dist in rnode_dist_pairs:
        print("%s\t%s %s" % (node, dest, dist))

    for node1, dist1 in rnode_dist_pairs:
        for node2, dist2 in rnode_dist_pairs:
            if(node1 != node2):
                print("%s\t%s %s" % (node1, node2, dist1+dist2))