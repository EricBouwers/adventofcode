#!/usr/bin/env python

import sys
from itertools import combinations 


example = "0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10"


def parse_comps(x):
    components = x.split("\n")
    components = map(lambda x: map(int, x.split("/")), components)
    return components


def get_value(comb):
    result = 0
    val = 0

    for i, c in enumerate(comb):
        if val in c:
            result += sum(c)
            val = sum(c) - val
        elif i < len(comb):
            return -1

    return result 


def next_paths(upto, pos, val):
    result = []

    for x in [y for y in pos if val in y]:
        tmp_upto = list(upto)
        tmp_upto.append(x)
        tmp_pos = list(pos)
        tmp_pos.remove(x)

        result.append((tmp_upto, tmp_pos, sum(x) - val))

    return result


def process_one(x):
    comps = parse_comps(x)
    all_paths = []
    prev_paths = [([], comps, 0)]
    added = 1  

    while added > 0:
        new_paths = []
        for upto, pos, val in prev_paths:
            new_paths += next_paths(upto, pos, val)

        added = len(new_paths)    
        all_paths += prev_paths
        prev_paths = new_paths

    results = map(lambda y: (len(y[0]), get_value(y[0])), all_paths)
    
    strongest = max(map(lambda x: x[1], results))

    longest_length = max(map(lambda x: x[0], results))
    strongest_longest = max(map(lambda y: y[1], filter(lambda x: x[0] == longest_length, results)))

    return strongest, strongest_longest


if __name__ == '__main__':
    assert process_one(example) == (31, 19)

    print process_one(sys.argv[1])
