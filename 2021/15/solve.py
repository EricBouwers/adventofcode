#!/usr/bin/env python
from collections import defaultdict
from functools import reduce
from operator import add

test_1 = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_map(m):
    cave_map = {}
    for y, l in enumerate(m):
        for x, v in enumerate(l):
            cave_map[(y, x)] = int(v)

    return cave_map


def neighbours(c):
    return [
        (c[0] + 1, c[1]),
        (c[0], c[1] + 1),
        (c[0], c[1] - 1),
        (c[0] - 1, c[1]),
    ]


def print_map(m):
    for y in range(0, 50):
        line = ''
        for x in range(0, 50):
            line += str(m[(y, x)]) + " "
        print(line)


def find_shortest(cave_map, paths, end):
    min_seens = {}
    while len(paths) > 0:
        cur_pos, risk = paths.pop(0)
        for s in neighbours(cur_pos):
            if s in cave_map:
                new_risk = risk + cave_map[s]
                if s == end:
                    return new_risk
                if s not in min_seens:
                    min_seens[s] = new_risk
                    paths.append((s, new_risk))
                    paths.sort(key=lambda x: x[1])


def part1(data, end=100):
    cave_map = parse_map(data)
    paths = [((0, 0), 0)]
    return find_shortest(cave_map, paths, (end-1, end-1))


def enlarge_cave_map(cave_map, s):
    new_y_cave_map = {}
    for c in cave_map:
        for d in range(0, 5):
            new_value = cave_map[c] + d
            new_value = (new_value % 9) if new_value > 9 else new_value
            new_y_cave_map[(c[0] + d * s, c[1])] = new_value

    new_cave_map = {}
    for c in new_y_cave_map:
        for d in range(0, 5):
            new_value = new_y_cave_map[c] + d
            new_value = (new_value % 9) if new_value > 9 else new_value
            new_cave_map[(c[0], c[1] + d * s)] = new_value

    return new_cave_map


def part2(data, orig_end=100):
    cave_map = parse_map(data)
    cave_map = enlarge_cave_map(cave_map, orig_end)
    paths = [((0, 0), 0)]
    return find_shortest(cave_map, paths, (orig_end*5-1, orig_end*5-1))


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 10) == 40
    assert part2(test_1.splitlines(), 10) == 315

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

