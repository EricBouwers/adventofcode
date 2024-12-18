#!/usr/bin/env python
import heapq
from collections import defaultdict
from heapq import heapify

test_1 = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""
test_2 = """"""


def parse_data(data):
    corrupt = []
    for d in data:
        x, y = d.split(',')
        corrupt.append((int(x), int(y)))
    return corrupt


def print_grid(grid, size):
    for y in range(size):
        line = ""
        for x in range(size):
            line += grid[(x, y)]

        print(line)


def find_path(grid, size):
    start = (0, 0)
    end = (size-1, size-1)
    paths = [(0, start)]
    heapify(paths)
    seens = defaultdict(lambda: 1000000)

    while paths:
        steps, coor = heapq.heappop(paths)
        if coor == end:
            return steps
        else:
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_c = (coor[0] + d[0], coor[1] + d[1])
                if new_c in grid and grid[new_c] != '#' and seens[new_c] > steps + 1:
                    heapq.heappush(paths, (steps+1, new_c))
                    seens[new_c] = steps+1

    return None


def part1(data, size=71, fallen=1024):
    corrupts = parse_data(data)
    grid = {(x, y): '.' for x in range(size) for y in range(size)}

    for i in range(fallen):
        grid[corrupts[i]] = '#'

    return find_path(grid, size)


def part2(data, size=71, fallen=1024):
    corrupts = parse_data(data)
    grid = {(x, y): '.' for x in range(size) for y in range(size)}

    for corrupt in corrupts:
        grid[corrupt] = '#'
        steps = find_path(grid, size)
        if steps is None:
            return corrupt


if __name__ == '__main__':

    assert part1(test_1.splitlines(), size=7, fallen=12) == 22
    assert part2(test_1.splitlines(), size=7, fallen=12) == (6, 1)

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

