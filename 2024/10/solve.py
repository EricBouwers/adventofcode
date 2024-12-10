#!/usr/bin/env python
import operator
from collections import defaultdict

test_1 = """0123
1234
8765
9876
"""
test_2 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


def parse_data(data):
    grid = defaultdict(lambda: -1)
    heads = []
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
            if c == '0':
                heads.append((x, y))

    return grid, heads


def take_step(pos, d):
    return tuple([operator.add(*x) for x in zip(pos, d)])


def get_steps(position, value, grid):
    steps = []
    for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_pos = take_step(position, dir)
        if (grid[new_pos] - 1) == value:
            steps.append((new_pos, grid[new_pos]))

    return steps


def paths(cur_pos, grid, unique=True):
    next_positions = [(cur_pos, grid[cur_pos])]
    ends = []
    while next_positions:
        new_positions = []
        for position in next_positions:
            if position[1] == 9:
                ends.append(position)
            else:
                new_positions += get_steps(position[0], position[1], grid)
        next_positions = new_positions

    return len(set(ends)) if unique else len(ends)


def part1(data):
    grid, heads = parse_data(data)
    return sum([paths(h, grid) for h in heads])


def part2(data):
    grid, heads = parse_data(data)
    return sum([paths(h, grid, False) for h in heads])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 1
    assert part1(test_2.splitlines()) == 36
    assert part2(test_2.splitlines()) == 81

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

