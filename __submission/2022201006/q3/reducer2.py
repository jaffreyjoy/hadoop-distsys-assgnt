#!/usr/bin/env python3
"""reducer2.py"""

import sys


source_node = '1'

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    node, rnode_dist_pairs  = line.split('\t', 1)
    if(node == source_node):
        rnode_dist_pairs = set([tuple([int(el) for el in  rnode_dist_pair.split(' ')]) for rnode_dist_pair in rnode_dist_pairs.split('\t')])
        for rnode, dist in rnode_dist_pairs:
            print("%s\t%s" % (rnode, dist))