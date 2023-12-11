#!/usr/bin/env python
from collections import defaultdict
from itertools import combinations

test_1 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
test_2 = """"""


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def parse_data(data, expand=1):
    grid = defaultdict(lambda: '.')
    galaxies = []
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == '#':
                galaxies.append((x, y))

    for y in range(len(data) - 1, -1, -1):
        if '#' not in data[y]:
            galaxies = [(g[0], g[1] + (0 if g[1] < y else expand)) for g in galaxies]

    for x in range(len(data[0]) - 1, -1, -1):
        col = [line[x] for line in data]
        if '#' not in col:
            galaxies = [(g[0] + (0 if g[0] < x else expand), g[1]) for g in galaxies]

    return galaxies


def part1(data):
    galaxies = parse_data(data, expand=1)
    return sum([distance(*x) for x in combinations(galaxies, 2)])


def part2(data, expand=9):
    galaxies = parse_data(data, expand=expand)
    return sum([distance(*x) for x in combinations(galaxies, 2)])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 374
    assert part2(test_1.splitlines()) == 1030
    assert part2(test_1.splitlines(), expand=99) == 8410

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines(), expand=999999))

