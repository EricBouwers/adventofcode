#!/usr/bin/env python
from collections import defaultdict

test_1 = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""
test_2 = """"""

DIRECTIONS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}


def take_step(dir, pos):
    return pos[0] + dir[0], pos[1] + dir[1]


def parse_data(data):
    grid = {}
    start = None
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == 'S':
                start = (x, y)
                grid[start] = '.'

    return grid, start


def part1(data, steps=64):
    grid, start = parse_data(data)

    cur_pos = [start]
    for s in range(0, steps):
        new_cur_pos = []
        for pos in cur_pos:
            for new_pos in [take_step(d, pos) for d in DIRECTIONS.values()]:
                if new_pos in grid and grid[new_pos] == '.':
                    new_cur_pos.append(new_pos)
        cur_pos = set(new_cur_pos)

    return len(cur_pos)


def part2(data, steps=26501365):
    grid, start = parse_data(data)

    max_x = len(data[0])
    max_y = len(data)
    cur_pos = {start: {(0, 0)}}
    seen_configs = {}
    for s in range(0, steps):
        new_cur_pos = defaultdict(lambda: set())
        for pos, grids in cur_pos.items():
            for new_pos in [take_step(d, pos) for d in DIRECTIONS.values()]:
                grid_shift = None
                if new_pos[0] == -1:
                    new_pos = (max_x-1, new_pos[1])
                    grid_shift = 'W'
                elif new_pos[0] == max_x:
                    new_pos = (0, new_pos[1])
                    grid_shift = 'E'
                elif new_pos[1] == -1:
                    new_pos = (new_pos[0], max_y-1)
                    grid_shift = 'N'
                elif new_pos[1] == max_y:
                    new_pos = (new_pos[0], 0)
                    grid_shift = 'S'

                if grid[new_pos] == '.':
                    new_cur_pos[new_pos].update(grids if grid_shift is None else {take_step(DIRECTIONS[grid_shift], g) for g in grids})

        cur_pos = new_cur_pos
        key = ",".join(map(str, cur_pos.keys()))
        if key in seen_configs:
            seen_configs[key][1].append(sum([len(x) for x in cur_pos.values()]))

            to_go = steps - s
            if to_go % 131 == 0:
                diffs = [t - s for s, t in zip(seen_configs[key][1], seen_configs[key][1][1:])]
                print(s, to_go / 131, seen_configs[key], diffs, [t - s for s, t in zip(diffs, diffs[1:])])
        else:
            seen_configs[key] = [s, [sum([len(x) for x in cur_pos.values()])]]

    return sum([len(x) for x in cur_pos.values()])


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 6) == 16
    assert part2(test_1.splitlines(), 6) == 16
    assert part2(test_1.splitlines(), 10) == 50
    assert part2(test_1.splitlines(), 100) == 6536
    assert part2(test_1.splitlines(), 500) == 167004

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    # print(part2(data.splitlines()))

    # based on eyeballing prints
    cur_count = 94909
    cur_diff = 60656
    diff_add = 30270
    start = 326
    cycle_length = 131
    for i in range(0, 202298):
        cur_diff += diff_add
        cur_count += cur_diff
        print(cur_count, start + ((i+1) * cycle_length))

