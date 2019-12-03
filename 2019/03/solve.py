#!/usr/bin/env python

import sys
from collections import defaultdict

test_0 = """R8,U5,L5,D3
U7,R6,D4,L4"""

test_1 = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""

test_2 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""

DIRECTIONS = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, -1),
    'U': (0, 1)
}


def man_dist(x, y):
    return sum([abs(x[i] - y[i]) for i in range(0, 2)])


def walk_line(grid, line_1, line):
    pos = (0, 0)
    steps = 0
    for ins in line_1:
        step = DIRECTIONS[ins[0]]

        for i in range(int(ins[1:])):
            steps += 1
            pos = (pos[0] + step[0], pos[1] + step[1])
            grid[pos].append((line, steps))


def print_grid(grid, x, y):

    for i in range(y):
        line = ""
        for j in range(x):
            wires = len([x[0] for x in grid[(j, i)]])
            line += "*" if wires == 2 else "+" if wires == 1 else "."

        print(line)


def part1(data):
    line_1 = data[0].split(',')
    line_2 = data[1].split(',')

    grid = defaultdict(list)

    walk_line(grid, line_1, 1)
    walk_line(grid, line_2, 2)

    min_dist = None
    for pos, lines in grid.items():
        if len(set([l[0] for l in lines])) > 1:
            min_dist = min(min_dist, man_dist((0, 0), pos)) if min_dist else man_dist((0, 0), pos)

    return min_dist


def part2(data):
    line_1 = data[0].split(',')
    line_2 = data[1].split(',')

    grid = defaultdict(list)

    walk_line(grid, line_1, 1)
    walk_line(grid, line_2, 2)

    combined_steps = None
    for pos, lines in grid.items():
        if len(set([l[0] for l in lines])) > 1:
            this_combined_steps = sum([l[1] for l in lines])
            combined_steps = min(this_combined_steps, combined_steps) if combined_steps else this_combined_steps

    return combined_steps


if __name__ == '__main__':

    assert part1(test_0.split("\n")) == 6
    assert part1(test_1.split("\n")) == 159
    assert part1(test_2.split("\n")) == 135
    assert part2(test_0.split("\n")) == 30
    assert part2(test_1.split("\n")) == 610
    assert part2(test_2.split("\n")) == 410

    with open(sys.argv[1]) as f:
        data = f.readlines()

    print(part1(data))
    print(part2(data))

