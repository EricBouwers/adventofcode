#!/usr/bin/env python

import sys
from collections import defaultdict

from int_code_comp import intcode_comp

test_1 = """"""
test_2 = """"""
test_3 = """"""
test_4 = """"""

DIRECTION_TO_STEPS = {
    "^" : [(0, 1), "<", ">"],
    "<": [(-1, 0), "v", "^"],
    "v": [(0, -1), ">", "<"],
    ">": [(1, 0), "^", "v"],
}


def part1(data, starting_color=0):
    memory = [int(x) for x in data.split(",")]
    pointer = 0

    grid = defaultdict(lambda: 0)
    cur_pos = (0, 0)
    grid[cur_pos] = starting_color

    facing = "^"
    painted = set()

    while True:
        memory, pointer, paint = intcode_comp(memory, [grid[cur_pos]], get_output=True, pointer=pointer)
        memory, pointer, output = intcode_comp(memory, [grid[cur_pos]], get_output=True, pointer=pointer)

        if paint is None or output is None:
            return len(painted), grid

        grid[cur_pos] = paint
        painted.add(cur_pos)

        facing = DIRECTION_TO_STEPS[facing][1+output]
        step = DIRECTION_TO_STEPS[facing][0]
        cur_pos = (cur_pos[0] + step[0], cur_pos[1] + step[1])


def part2(data):
    _, grid = part1(data, 1)
    for y in range(10):
        line = ""
        for x in range(-100, 100):
            line += " " if grid[(x, y)] == 0 else "#"
        print(line)


if __name__ == '__main__':

    # assert part1(test_1) == None
    # assert part1(test_2) == None
    # assert part2(test_3) == None
    # assert part2(test_4) == None

    with open('input') as f:
        data = f.readlines()

    # print(part1(data[0])[0])
    print(part2(data[0]))

