#!/usr/bin/env python
from collections import defaultdict, Counter

test_1 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""
test_2 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

test_3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

test_4 = """..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
.........."""

test_5 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

test_6 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

PIPES = {
    '|': lambda x: x,
    '-': lambda x: x,
    'L': lambda x: RIGHT if x == DOWN else UP if x == LEFT else None,
    'J': lambda x: LEFT if x == DOWN else UP if x == RIGHT else None,
    '7': lambda x: LEFT if x == UP else DOWN if x == RIGHT else None,
    'F': lambda x: RIGHT if x == UP else DOWN if x == LEFT else None,
    '.': lambda x: None,
}


def step(cur, direction):
    return cur[0] + direction[0], cur[1] + direction[1]


def parse_data(data):
    start = None
    grid = defaultdict(lambda: '.')

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == 'S':
                start = (x, y)
            else:
                grid[(x, y)] = c

    start_dirs = []
    if grid[step(start, UP)] in "|7F":
        start_dirs.append(UP)
    if grid[step(start, DOWN)] in "|LJ":
        start_dirs.append(DOWN)
    if grid[step(start, LEFT)] in "-LF":
        start_dirs.append(LEFT)
    if grid[step(start, RIGHT)] in "-J7":
        start_dirs.append(RIGHT)

    if start_dirs[0] == UP:
        if start_dirs[1] == DOWN:
            grid[start] = '|'
        elif start_dirs[1] == LEFT:
            grid[start] = 'J'
        elif start_dirs[1] == RIGHT:
            grid[start] = 'L'
    elif start_dirs[0] == DOWN:
        if start_dirs[1] == LEFT:
            grid[start] = '7'
        elif start_dirs[1] == RIGHT:
            grid[start] = 'F'
    else:
        grid[start] = '-'

    return start, start_dirs, grid


def part1(data):
    start, start_dirs, grid = parse_data(data)

    cur_state = [(start, start_dirs[0]), (start, start_dirs[1])]
    steps = 0
    while len(set([s[0] for s in cur_state])) != 1 or cur_state[0][0] == start:
        steps += 1
        new_state = []
        for state in cur_state:
            new_pos = step(*state)
            new_dir = PIPES[grid[new_pos]](state[1])
            new_state.append((new_pos, new_dir))
        cur_state = new_state

    return steps


def part2(data):
    start, start_dirs, grid = parse_data(data)

    cur_state = (start, start_dirs[1])
    pipe_coords = []

    while start not in pipe_coords:
        new_pos = step(*cur_state)
        new_dir = PIPES[grid[new_pos]](cur_state[1])
        cur_state = (new_pos, new_dir)
        pipe_coords.append(new_pos)

    # shoelace solution
    shoe_surface = 0
    for p1, p2 in zip(pipe_coords, pipe_coords[1:] + [pipe_coords[0]]):
        shoe_surface += p1[0] * p2[1] - p1[1] * p2[0]

    shoe_surface = abs(shoe_surface / 2)
    shoe_surface = int(shoe_surface) - len(pipe_coords)/2 + 1

    # trace
    trace_surface = 0
    for y in range(0, len(data)):
        inside = False
        for x in range(0, len(data[0])):
            if grid[(x, y)] in '|7F' and (x, y) in pipe_coords:
                inside = not inside
            elif (x, y) not in pipe_coords:
                trace_surface += 1 if inside else 0

    return shoe_surface


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 4
    assert part1(test_2.splitlines()) == 8
    assert part2(test_1.splitlines()) == 1
    assert part2(test_3.splitlines()) == 4
    assert part2(test_4.splitlines()) == 4
    assert part2(test_5.splitlines()) == 8
    assert part2(test_6.splitlines()) == 10

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

