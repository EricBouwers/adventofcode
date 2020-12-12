#!/usr/bin/env python
from collections import deque

test_1 = """F10
N3
F7
R90
F11"""
test_2 = """"""
test_3 = """"""
test_4 = """"""

STEPS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}


def part1(data):
    cur_dir = 'E'
    cur_coor = (0, 0)
    directions = deque('ESWN')
    for stm in data:
        ins = stm[0]
        ins = cur_dir if ins == 'F' else ins
        steps = int(stm[1:])
        if ins in STEPS:
            cur_coor = (cur_coor[0] + (steps * STEPS[ins][0]),
                        cur_coor[1] + (steps * STEPS[ins][1]))
        else:
            change = -int(steps/90) if ins == 'R' else int(steps/90)
            directions.rotate(change)
            cur_dir = directions[0]

    return abs(cur_coor[0]) + abs(cur_coor[1])


def part2(data):
    ship_coor = (0, 0)
    wp_coor = (10, 1)
    for stm in data:
        ins = stm[0]
        steps = int(stm[1:])
        if ins == 'F':
            ship_coor = (ship_coor[0] + (steps * wp_coor[0]),
                         ship_coor[1] + (steps * wp_coor[1]))
        elif ins in STEPS:
            wp_coor = (wp_coor[0] + (steps * STEPS[ins][0]),
                       wp_coor[1] + (steps * STEPS[ins][1]))
        else:
            rotations = int(steps/90) if ins == 'R' else 4 - int(steps/90)
            for _ in range(0, rotations):
                wp_coor = (wp_coor[1], -wp_coor[0])

    return abs(ship_coor[0]) + abs(ship_coor[1])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 25
    assert part2(test_1.splitlines()) == 286

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

