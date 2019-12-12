#!/usr/bin/env python

import sys
from collections import defaultdict

from int_code_comp import intcode_comp

test_1 = """"""
test_2 = """"""
test_3 = """"""
test_4 = """"""

DIRECTION_TO_STEPS = {
    "^": [(0, -1), "<", ">"],
    "<": [(-1, 0), "v", "^"],
    "v": [(0, 1), ">", "<"],
    ">": [(1, 0), "^", "v"],
}


def part1(data, starting_color=0):
    memory = [int(x) for x in data.split(",")]
    pointer = 0
    relative_pointer = 0

    grid = defaultdict(lambda: 0)
    cur_pos = (0, 0)
    grid[cur_pos] = starting_color

    facing = "^"
    painted = set()

    while True:
        memory, pointer, paint, relative_pointer = intcode_comp(memory, [grid[cur_pos]], get_output=True, pointer=pointer, relative_pointer=relative_pointer)
        memory, pointer, output, relative_pointer = intcode_comp(memory, [grid[cur_pos]], get_output=True, pointer=pointer, relative_pointer=relative_pointer)

        grid[cur_pos] = paint
        painted.add(cur_pos)

        if paint is None or output is None:
            return len(painted), grid

        facing = DIRECTION_TO_STEPS[facing][1+output]
        step = DIRECTION_TO_STEPS[facing][0]
        cur_pos = (cur_pos[0] + step[0], cur_pos[1] + step[1])


def part2(data):
    _, grid = part1(data, 1)
    for y in range(0, 10):
        line = ""
        for x in range(-50, 100):
            line += " " if grid[(x, y)] == 0 else "#"
        print(line)


if __name__ == '__main__':
    with open('input') as f:
        data = f.readlines()

    print(part1(data[0])[0])
    print(part2(data[0]))

