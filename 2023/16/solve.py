#!/usr/bin/env python
from collections import defaultdict

test_1 = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""
test_2 = """"""

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

NEXT_DIRS = {
    '.': lambda d: [d],
    '|': lambda d: [d] if d in [UP, DOWN] else [UP, DOWN],
    '-': lambda d: [d] if d in [LEFT, RIGHT] else [LEFT, RIGHT],
    '\\': lambda d: {LEFT: [UP], RIGHT: [DOWN], UP: [LEFT], DOWN: [RIGHT]}[d],
    '/': lambda d: {LEFT: [DOWN], RIGHT: [UP], UP: [RIGHT], DOWN: [LEFT]}[d],
}


def take_step(dir, pos):
    return pos[0] + dir[0], pos[1] + dir[1]


def parse_data(data):
    grid = {}
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            grid[(x, y)] = c
    return grid


def calc_energized(grid, coor, direction):
    beams = [(coor, direction)]
    energized = defaultdict(lambda: set())
    while beams:
        coor, direction = beams.pop()
        if coor in grid:
            if direction not in energized[coor]:
                energized[coor].add(direction)
                for next_dir in NEXT_DIRS[grid[coor]](direction):
                    beams.append((take_step(next_dir, coor), next_dir))

    return len(energized.keys())


def part1(data):
    grid = parse_data(data)
    return calc_energized(grid, (0, 0), RIGHT)


def part2(data):
    grid = parse_data(data)

    max_y = len(data)
    max_x = len(data[0])
    max_energy = 0
    for x in range(0, max_x):
        max_energy = max([
            max_energy,
            calc_energized(grid, (x, 0), DOWN),
            calc_energized(grid, (x, max_y - 1), UP)
        ])
    for y in range(0, max_y):
        max_energy = max([
            max_energy,
            calc_energized(grid, (0, y), RIGHT),
            calc_energized(grid, (max_x - 1, y), LEFT)
        ])

    return max_energy


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 46
    assert part2(test_1.splitlines()) == 51

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
