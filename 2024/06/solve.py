#!/usr/bin/env python
from collections import defaultdict

test_1 = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
test_2 = """"""

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def parse_data(data):
    grid = defaultdict(lambda: None)
    start_pos = None
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == '^':
                start_pos = (x, y)
                grid[(x, y)] = '.'

    return grid, start_pos


def take_step(pos, d):
    return (pos[0] + DIRECTIONS[d][0],
            pos[1] + DIRECTIONS[d][1])


def has_loop(grid, cur_pos):
    direction = 0 if grid[take_step(cur_pos, 0)] == '.' else 1
    path = {cur_pos}

    while grid[cur_pos] is not None:
        cur_pos = take_step(cur_pos, direction)

        if (cur_pos, direction) not in path:
            path.add((cur_pos, direction))
        else:
            cur_pos = (-10, -10)

        while grid[take_step(cur_pos, direction)] == '#':
            direction = (direction + 1) % 4

    return cur_pos == (-10, -10)


def get_path(grid, cur_pos):
    path = {cur_pos}
    direction = 0

    while grid[cur_pos] is not None:
        cur_pos = take_step(cur_pos, direction)
        if grid[cur_pos] is not None:
            path.add(cur_pos)

        if grid[take_step(cur_pos, direction)] == '#':
            direction = (direction + 1) % 4

    return path


def part1(data):
    grid, cur_pos = parse_data(data)
    return len(get_path(grid, cur_pos))


def part2(data):
    grid, cur_pos = parse_data(data)
    possible_spaces = []
    empty_spaces = get_path(grid, cur_pos)

    for p in empty_spaces:
        changed_grid = grid.copy()
        changed_grid[p] = '#'
        if has_loop(changed_grid, cur_pos):
            possible_spaces.append(p)

    return len(possible_spaces)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 41
    assert part2(test_1.splitlines()) == 6

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
