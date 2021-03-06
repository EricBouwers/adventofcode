#!/usr/bin/env python

import sys, re, itertools

test_input = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def part1(data):
    points = [map(int, re.findall('[0-9]+', line)) for line in data.split("\n")]
    squares = {}        
    infinites = set()

    size = max(max([x[0] for x in points]), max([y[1] for y in points])) + 1
    
    for x in range(0,size):
        for y in range(0,size):
            best_dist = size * 2
            best_val = None
           
            for i, point in enumerate(points):
                cur_dist = distance([x,y], point)
                
                if cur_dist == best_dist:
                    best_val = None
                
                if cur_dist < best_dist:
                    best_dist = cur_dist
                    best_val = i

            if best_val is not None:
                if best_val not in squares.keys():
                    squares[best_val] = set()
                squares[best_val].add((x,y))    

                if x in [0, size-1] or y in [0,size-1]:
                    infinites.add(best_val)

    largest_square = 0
    for square in squares.keys():
        if square not in infinites:
            cur_size = len(squares[square]) 
            if cur_size > largest_square:
                largest_square = cur_size

    return largest_square 

def part2(data, val):
    points = [map(int, re.findall('[0-9]+', line)) for line in data.split("\n")]
    area = 0

    biggest_diff = sum(map(lambda ps: distance(ps[0],ps[1]), [x for x in itertools.permutations(points, 2)]))
    if biggest_diff > val:
        min_x = min([x[0] for x in points])
        min_y = min([y[1] for y in points])
        max_x = max([x[0] for x in points])
        max_y = max([y[1] for y in points])
    else:
        min_x, min_y, max_x, max_y = (0,0,val,val)

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            area += 1 if sum(map(lambda p: distance([x,y], p), points)) < val else 0

    return area

if __name__ == '__main__':

    assert part1(test_input) == 17
    assert part2(test_input, 32) == 16 

    data = sys.argv[1]

    print part1(data)
    print part2(data, 10000)

