#!/usr/bin/env python

import sys, re

example_input_1 = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""


def collect_nearby(area, cur_x, cur_y, max_y, max_x):
    stats = {".":0, "|":0,"#":0}

    for y in [cur_y-1, cur_y, cur_y+1]:
        for x in [cur_x-1, cur_x, cur_x+1]:
            if all([0 <= y, y < max_y, 0 <= x, x < max_x]):
                stats[area[y][x]] += 1

    stats[area[cur_y][cur_x]] -= 1            
    return stats

def part1(data, minutes):

    area = [[x for x in y] for y in data.split("\n")]
    max_y = len(area)
    max_x = len(area[0])

    seen = {}
    m = 0
    
    while m < minutes:
        new_area = []
        for y in range(0, max_y):
            new_y = []
            new_area.append(new_y)
            for x in range(0, max_x):
                stats = collect_nearby(area, x, y, max_y, max_x)
                new_char = None
                if area[y][x] == ".":
                    new_char = "|" if stats["|"] >= 3 else "."
                if area[y][x] == "|":
                    new_char = "#" if stats["#"] >= 3 else "|"
                if area[y][x] == "#":
                    new_char = "#" if stats["#"] >= 1 and stats["|"] >= 1 else "."
                new_y.append(new_char)
        area = new_area 

        printed = print_area(area)
        if printed in seen.keys():
            print "fast forward", m, seen[printed]
            diff = m - seen[printed][0]
            while m < minutes:
                m += diff
            
            # We need to step one forward ... 
            m -= (diff - 1)    
            seen = {}  
        else:
            seen[printed] = (m, calc_value(area, max_x, max_y))
            m += 1

    return calc_value(area, max_x, max_y)


def calc_value(area, max_x, max_y):
    trees = 0
    yards = 0
    for y in range(0, max_y):
        for x in range(0, max_x):
            trees += 1 if area[y][x] == "|" else 0
            yards += 1 if area[y][x] == "#" else 0
    
    return trees * yards

def print_area(area):
    result = "\n".join(["".join(y) for y in area])
    print result
    return result

if __name__ == '__main__':

    assert part1(example_input_1,10) == 1147

    data = sys.argv[1]

    print part1(data,10)
    print part1(data,1000000000)

