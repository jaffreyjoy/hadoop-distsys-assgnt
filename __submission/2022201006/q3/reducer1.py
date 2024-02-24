#!/usr/bin/env python3
"""reducer1.py"""

import sys


prev_node = None
combined_rnode_dist_map = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    node, rnode_dist_pairs  = line.split('\t', 1)
    rnode_dist_pairs = set([tuple([int(el) for el in  rnode_dist_pair.split(' ')]) for rnode_dist_pair in rnode_dist_pairs.split('\t')])
    rnode_dist_map = {}
    for rnode, dist in rnode_dist_pairs:
        rnode_dist_map[rnode] = dist

    if node == prev_node:
        for rnode, dist in rnode_dist_map.items():
            if(rnode in combined_rnode_dist_map):
                combined_rnode_dist_map[rnode] = min(combined_rnode_dist_map[rnode], dist)
            else:
                combined_rnode_dist_map[rnode] = dist
    else:
        if prev_node:
            rnode_dist_pairs = [f"{rnode} {dist}" for rnode, dist in combined_rnode_dist_map.items()]
            print("%s\t%s" %(prev_node, "\t".join(rnode_dist_pairs)))
        prev_node = node
        combined_rnode_dist_map = rnode_dist_map
if prev_node:
    rnode_dist_pairs = [f"{rnode} {dist}" for rnode, dist in combined_rnode_dist_map.items()]
    print("%s\t%s" %(prev_node, "\t".join(rnode_dist_pairs)))
