#!/usr/bin/env python

import sys

test_1 = """....#
#..#.
#..##
..#..
#...."""
test_2 = """....#
#..#.
#.?##
..#..
#...."""


def parse_world(data):
    world = {}
    y = 0
    for l in data.splitlines():
        x = 0
        for c in l:
            world[(x, y)] = c
            x += 1
        y += 1

    return world


def print_world(world, sep="\n", start=0, end=5):
    output = ""
    for y in range(start, end):
        for x in range(start, end):
            output += world[(x, y)]
        output += sep
    print(output)

    return output


def calc_adjacent(cur_pos, step):
    return cur_pos[0] + step[0], cur_pos[1] + step[1]


STEPS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
NORMAL_STEPS = {
    (x, y): [
        p for p in map(lambda s: calc_adjacent((x, y), s), STEPS) if 0 <= p[0] < 5 and 0 <= p[1] < 5
    ] for x in range(5) for y in range(5)
}


def count_adjacent(world, cur_pos, what):
    return sum([what == world.get(s, "") for s in NORMAL_STEPS[cur_pos]])


def next_world(world):
    new_world = {}

    for k, v in world.items():
        if v == "#" and count_adjacent(world, k, "#") != 1:
            v = "."
        elif v == "." and count_adjacent(world, k, "#") in [1, 2]:
            v = "#"
        new_world[k] = v

    return new_world


def part1(data):
    world = parse_world(data)

    seens = set()
    new_world = print_world(world, sep="")

    while new_world not in seens:
        seens.add(new_world)
        world = next_world(world)
        new_world = print_world(world, sep="")

    return sum([0 if c == "." else 2**i for i, c in enumerate(new_world)])


INNERS = set(set([(x, y) for x in range(1, 4) for y in range(1, 4)]))
INNERS = INNERS - {(2, 2)}


def needs_inner(world):
    return sum([world[i] == "#" for i in INNERS]) > 0


OUTERS = set([(x, y) for x in range(5) for y in range(5)])
OUTERS = OUTERS - INNERS
OUTERS = OUTERS - {(2, 2)}


def needs_outer(world):
    return sum([world[i] == "#" for i in OUTERS]) > 0


def new_level():
    level = {(x, y): "." for x in range(5) for y in range(5)}
    level[(2, 2)] = "?"
    return level


RECURSIVE_STEPS = {
    k: [(0, p) for p in v if p != (2, 2)] for k, v in NORMAL_STEPS.items()
}

CONNECTIONS = {
    (2, 1): [(i, 0) for i in range(5)],
    (1, 2): [(0, i) for i in range(5)],
    (3, 2): [(4, i) for i in range(5)],
    (2, 3): [(i, 4) for i in range(5)]
}

for k, v in CONNECTIONS.items():
    RECURSIVE_STEPS[k] += [(1, p) for p in v]
    for p in v:
        RECURSIVE_STEPS[p].append((-1, k))


def count_adjacent_recursive(level_index, levels, cur_pos, what):
    return sum([what == levels.get(level_index+i, {p: ""})[p] for i, p in RECURSIVE_STEPS[cur_pos]])


def next_world_recursive(level_world, level_index, levels):
    new_world = {}

    for k, v in level_world.items():
        if v == "#" and count_adjacent_recursive(level_index, levels, k, "#") != 1:
            v = "."
        elif v == "." and count_adjacent_recursive(level_index, levels, k, "#") in [1, 2]:
            v = "#"
        new_world[k] = v

    return new_world


def next_levels(levels):
    new_levels = {}
    level_indexes = sorted(levels.keys())
    min_level = level_indexes[0]
    max_level = level_indexes[-1]

    if needs_inner(levels[min_level]):
        levels[min_level - 1] = new_level()
    if needs_outer(levels[max_level]):
        levels[max_level + 1] = new_level()

    for level_index, level_world in levels.items():
        level_world = next_world_recursive(level_world, level_index, levels)
        new_levels[level_index] = level_world

    return new_levels


def part2(data, minutes):
    world = parse_world(data)
    world[(2, 2)] = "?"

    levels = {0: world}

    for _ in range(minutes):
        levels = next_levels(levels)

    bugs = 0
    for l in levels:
        print(l)
        print_world(levels[l], sep="\n")
        bugs += sum([c == "#" for c in levels[l].values()])
    return bugs


if __name__ == '__main__':

    assert part1(test_1) == 2129920
    assert part2(test_2, 10) == 99

    with open('input') as f:
        data = f.read()

    print(part1(data))
    print(part2(data, 200))

