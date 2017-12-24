#!/usr/bin/env python

import sys
from itertools import combinations 


example = "0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10"


def parse_comps(x):
    components = x.split("\n")
    components = map(lambda x: map(int, x.split("/")), components)
    return components


def next_paths(l, v, pos, val):
    result = []

    for x in [y for y in pos if val in y]:
        tmp_pos = list(pos)
        tmp_pos.remove(x)

        result.append((l+1, v+sum(x), tmp_pos, sum(x) - val))

    return result


def process_one(x):
    comps = parse_comps(x)
    all_paths = []
    prev_paths = [(0, 0, comps, 0)]
    added = 1  

    while added > 0:
        new_paths = []
        for l, v, pos, val in prev_paths:
            new_paths += next_paths(l, v, pos, val)

        added = len(new_paths)    
        all_paths += prev_paths
        prev_paths = new_paths

    strongest = max(map(lambda x: x[1], all_paths))

    longest_length = max(map(lambda x: x[0], all_paths))
    strongest_longest = max(map(lambda y: y[1], filter(lambda x: x[0] == longest_length, all_paths)))

    return strongest, strongest_longest


if __name__ == '__main__':
    assert process_one(example) == (31, 19)

    print process_one(sys.argv[1])
