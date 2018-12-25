#!/usr/bin/env python

import sys, re, collections, itertools

example_input_1 = """ 0,0,0,0
 3,0,0,0
 0,3,0,0
 0,0,3,0
 0,0,0,3
 0,0,0,6
 9,0,0,0
12,0,0,0"""

example_input_2 = """-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0"""

example_input_3 = """1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2"""

example_input_4 = """1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2"""

def dist(x,y):
    return sum(map(lambda x: abs(x[0]-x[1]), zip(x,y)))

def part1(data):
    points = [tuple(map(int, re.findall("-?\d+", line))) for line in data.split("\n")]
    together = collections.defaultdict(set)

    for p1 in points:
        for p2 in points:
            if dist(p1, p2) <= 3:
                together[p1].add(p2)

    constellations = together.values()
    cur_length = len(constellations)
    prev_length = cur_length + 1

    while prev_length > cur_length:
        prev_length = cur_length
        
        new_constellations = [constellations.pop()]

        for c1 in constellations:
            merge_with = None
            for c2 in new_constellations:
                if len(c1.intersection(c2)) > 0:
                    merge_with = c2
        
            if merge_with:
                merge_with.update(c1)
            else:
                new_constellations.append(c1)

        constellations = new_constellations
        cur_length = len(constellations)

    return cur_length

if __name__ == '__main__':

    assert part1(example_input_1) == 2
    assert part1(example_input_2) == 4
    assert part1(example_input_3) == 3
    assert part1(example_input_4) == 8

    data = sys.argv[1]

    print part1(data)
