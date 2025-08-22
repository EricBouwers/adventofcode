#!/usr/bin/env python
from collections import defaultdict

test_1 = """.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""
test_2 = """"""


def parse_data(data):
    grid = defaultdict(lambda: False)
    max_y, max_x = 0, 0

    for y, l in enumerate(data):
        for x, c in enumerate(l):
            grid[(y,x)] = c == '#'
            max_y = max([max_y, y])
            max_x = max([max_x, x])

    return grid, max_x, max_y

def print_grid(grid, max_x, max_y):
    for y in range(0, max_y+1):
        line = []
        for x in range(0, max_x+1):
            line.append("#" if grid[(y,x)] else '.')
        print("".join(line))
    print()

def should_turn_on_part_1(grid, x, y, max_x, max_y):
    on_neighbours = sum([
        grid[(y - 1, x - 1)], grid[(y - 1, x)], grid[(y - 1, x + 1)],
        grid[(y, x - 1)], grid[(y, x + 1)],
        grid[(y + 1, x - 1)], grid[(y + 1, x)], grid[(y + 1, x + 1)],
    ])
    return (grid[(y, x)] and on_neighbours == 2) or on_neighbours == 3

def should_turn_on_part_2(grid, x, y, max_x, max_y):
    return (x,y) in [(0,0), (max_y, 0), (0, max_x), (max_y, max_x)] or should_turn_on_part_1(grid, x, y, max_x, max_y)

def calculate_lights(grid, max_x, max_y, steps, light_function):
    for s in range(0, steps):
        new_grid = defaultdict(lambda: False)
        for y in range(0, max_y+1):
            for x in range(0, max_x+1):
                new_grid[(y, x)] = light_function(grid, x, y, max_x, max_y)
        grid = new_grid

    return sum(grid.values())

def part1(data, steps=100):
    grid, max_x, max_y = parse_data(data)
    return calculate_lights(grid, max_x, max_y, steps, should_turn_on_part_1)

def part2(data, steps=100):
    grid, max_x, max_y = parse_data(data)
    grid[(0, 0)] = True
    grid[(0, max_x)] = True
    grid[(max_y, 0)] = True
    grid[(max_y, max_x)] = True

    return calculate_lights(grid, max_x, max_y, steps, should_turn_on_part_2)


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 4) == 4
    assert part2(test_1.splitlines(), 5) == 17

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

