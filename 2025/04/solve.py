#!/usr/bin/env python
from collections import defaultdict

test_1 = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
test_2 = """"""


def parse_data(data):
    grid = defaultdict(lambda: None)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x,y)] = c
    return grid


def get_neighbours(x, y):
    return [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x + 1, y),                 (x + 1, y + 1),
        (x, y + 1), (x - 1, y + 1), (x - 1, y)]

def part1(data):
    grid = parse_data(data)

    total = 0
    for x,y in list(grid.keys()):
        neighbours_rolls = sum([grid[(a,b)] == "@" for a,b in get_neighbours(x, y)])
        total += 1 if neighbours_rolls < 4 and grid[(x,y)] == "@" else 0

    return total


def part2(data):
    grid = parse_data(data)

    total = 0
    prev_total = -1

    keys_to_check = [p for p in grid.keys() if grid[p] == "@"]

    while total != prev_total:
        to_remove = []
        for x,y in keys_to_check:
            neighbours_rolls = sum([grid[(a,b)] == "@" for a,b in get_neighbours(x, y)])
            if neighbours_rolls < 4:
                to_remove.append((x,y))
        prev_total = total
        total += len(to_remove)
        for p in to_remove:
            grid[p] = "."
        keys_to_check = [p for p in grid.keys() if grid[p] == "@"]

    return total


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 13
    assert part2(test_1.splitlines()) == 43

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

