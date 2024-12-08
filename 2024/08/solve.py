#!/usr/bin/env python
import itertools
from collections import defaultdict

test_1 = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
test_2 = """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
..........
"""


def parse_data(data):
    antennas = defaultdict(lambda: list())
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c != '.':
                antennas[c].append((x, y))

    return antennas, len(data[0]), len(data)


def part1(data):
    antennas, max_x, max_y = parse_data(data)

    antinodes = set()
    for antenna in antennas.keys():
        for a1, a2 in itertools.combinations(antennas[antenna], 2):
            x_diff = a1[0] - a2[0]
            y_diff = a1[1] - a2[1]
            antinodes.add((a1[0] + x_diff, a1[1] + y_diff))
            antinodes.add((a2[0] - x_diff, a2[1] - y_diff))

    return len([c for c in antinodes if 0 <= c[0] < max_x and 0 <= c[1] < max_y])


def part2(data):
    antennas, max_x, max_y = parse_data(data)

    antinodes = set()
    for antenna in antennas.keys():
        for a1, a2 in itertools.combinations(antennas[antenna], 2):
            x_diff = a1[0] - a2[0]
            y_diff = a1[1] - a2[1]

            new_pos = (a1[0] + x_diff, a1[1] + y_diff)
            in_bounds = 0 <= new_pos[0] < max_x and 0 <= new_pos[1] < max_y
            while in_bounds:
                antinodes.add(new_pos)
                new_pos = (new_pos[0] + x_diff, new_pos[1] + y_diff)
                in_bounds = 0 <= new_pos[0] < max_x and 0 <= new_pos[1] < max_y

            new_pos = (a2[0] - x_diff, a2[1] - y_diff)
            in_bounds = 0 <= new_pos[0] < max_x and 0 <= new_pos[1] < max_y
            while in_bounds:
                antinodes.add(new_pos)
                new_pos = (new_pos[0] - x_diff, new_pos[1] - y_diff)
                in_bounds = 0 <= new_pos[0] < max_x and 0 <= new_pos[1] < max_y

    for v in [x for x in antennas.values() if len(x) > 1]:
        antinodes.update(set(v))

    return len(antinodes)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 14
    assert part2(test_2.splitlines()) == 9
    assert part2(test_1.splitlines()) == 34

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))


# 366 too high