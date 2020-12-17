#!/usr/bin/env python
from collections import defaultdict
from itertools import permutations

test_1 = """.#.
..#
###"""


NEIGHBOURS_3D = set([x for x in permutations([-1, -1, -1, 0, 0, 1, 1, 1], 3)])
NEIGHBOURS_4D = set([x for x in permutations([-1, -1, -1, -1, 0, 0, 0, 1, 1, 1, 1], 4)])


def part1(data):
    space = defaultdict(lambda: 0)
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            space[(r, c, 0)] = 1 if col == '#' else 0

    for c in range(0, 6):
        new_space = defaultdict(lambda: 0)
        for coor in [c for c, a in space.items() if a == 1]:
            for x, y, z in [coor] + [(coor[0]+n[0], coor[1]+n[1], coor[2]+n[2]) for n in NEIGHBOURS_3D]:
                active_neighbours = sum([space[(x+n[0], y+n[1], z+n[2])] for n in NEIGHBOURS_3D])
                if space[(x, y, z)] == 1:
                    new_space[(x, y, z)] = 1 if active_neighbours in [2, 3] else 0
                else:
                    new_space[(x, y, z)] = 1 if active_neighbours in [3] else 0
        space = new_space

    return sum(space.values())


def part2(data):
    space = defaultdict(lambda: 0)
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            space[(r, c, 0, 0)] = 1 if col == '#' else 0

    for c in range(0, 6):
        new_space = defaultdict(lambda: 0)
        for coor in [c for c, a in space.items() if a == 1]:
            for x, y, z, w in [coor] + [(coor[0]+n[0], coor[1]+n[1], coor[2]+n[2], coor[3]+n[3]) for n in NEIGHBOURS_4D]:
                if (x, y, z, w) not in new_space:
                    active_neighbours = sum([space[(x+n[0], y+n[1], z+n[2], w+n[3])] for n in NEIGHBOURS_4D])
                    if space[(x, y, z, w)] == 1:
                        new_space[(x, y, z, w)] = 1 if active_neighbours in [2, 3] else 0
                    else:
                        new_space[(x, y, z, w)] = 1 if active_neighbours in [3] else 0
        space = new_space

    return sum(space.values())


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 112
    assert part2(test_1.splitlines()) == 848

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

