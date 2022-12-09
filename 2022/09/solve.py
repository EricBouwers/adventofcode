#!/usr/bin/env python
from math import dist

test_1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
test_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


DIRS = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}


def parse_steps(data):
    return [(DIRS[d.split(" ")[0]], int(d.split(" ")[1])) for d in data]


def take_step(dir, pos):
    return pos[0] + dir[0], pos[1] + dir[1]


def drag_tail(h_pos, t_pos):
    if dist(h_pos, t_pos) < 2:
        return t_pos
    else:
        if h_pos[0] == t_pos[0]:
            return t_pos[0], t_pos[1] + (1 if t_pos[1] < h_pos[1] else -1)
        elif h_pos[1] == t_pos[1]:
            return t_pos[0] + (1 if t_pos[0] < h_pos[0] else -1), t_pos[1]
        else:
            return t_pos[0] + (1 if t_pos[0] < h_pos[0] else -1), t_pos[1] + (1 if t_pos[1] < h_pos[1] else -1)


def part1(data):
    steps = parse_steps(data)
    h_pos = (0, 0)
    t_pos = (0, 0)
    visited_pos = set()

    for step in steps:
        for s in range(0, step[1]):
            h_pos = take_step(step[0], h_pos)
            t_pos = drag_tail(h_pos, t_pos)
            visited_pos.add(t_pos)

    return len(visited_pos)


def part2(data):
    steps = parse_steps(data)
    h_pos = (0, 0)
    t_positions = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    visited_pos = set()

    for step in steps:
        for s in range(0, step[1]):
            h_pos = take_step(step[0], h_pos)

            cur_h = h_pos
            for i in range(0, len(t_positions)):
                t_positions[i] = drag_tail(cur_h, t_positions[i])
                cur_h = t_positions[i]

            visited_pos.add(t_positions[8])

    return len(visited_pos)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 13
    assert part2(test_1.splitlines()) == 1
    assert part2(test_2.splitlines()) == 36

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

