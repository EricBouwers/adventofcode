#!/usr/bin/env python
import math
import sys

from int_code_comp import intcode_comp

test_1 = """"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_world(data, start=0, end=50):
    memory = [int(x) for x in data.split(",")]
    pointer = 0
    relative_pointer = 0
    world = {}

    for x in range(start, end):
        for y in range(start, end):
            _, _, s, _ = intcode_comp(memory, [x, y], True, pointer, relative_pointer)
            world[(x, y)] = s

    return world


def print_world(world, start=0, end=50):
    for y in range(start, end):
        line = ""
        for x in range(start, end):
            line += "." if world[(x, y)] == 0 else "#"
        print(line)


def part1(data):
    world = parse_world(data)
    print_world(world)

    return sum(world.values())


def get_x(y, approx):
    return math.ceil(y*approx)


def part2(data):
    memory = [int(x) for x in data.split(",")]
    pointer = 0
    relative_pointer = 0

    approximation = 2

    y = 100
    found = False
    while not found:
        if y % 1000 == 0:
            print(y)

        x = get_x(y, approximation)
        _, _, left_bottom, _ = intcode_comp(memory, [x, y], True, pointer, relative_pointer)
        _, _, check, _ = intcode_comp(memory, [x-1, y], True, pointer, relative_pointer)

        while check == 1:
            approximation = (x-1)/y
            x = get_x(y, approximation)

            _, _, left_bottom, _ = intcode_comp(memory, [x, y], True, pointer, relative_pointer)
            _, _, check, _ = intcode_comp(memory, [x-1, y], True, pointer, relative_pointer)

        assert left_bottom == 1 and check == 0, "{}, {}".format(x, y)

        _, _, right_bottom, _ = intcode_comp(memory, [x + 99, y], True, pointer, relative_pointer)

        if left_bottom == 1 and right_bottom == 1:
            _, _, left_top, _ = intcode_comp(memory, [x, y - 99], True, pointer, relative_pointer)
            if left_top == 1:
                _, _, right_top, _ = intcode_comp(memory, [x + 99, y - 99], True, pointer, relative_pointer)
                found = right_top == 1

        if not found:
            y = y + 1

    return x * 10000 + y - 99


if __name__ == '__main__':

    with open('input') as f:
        data = f.read()

    print(part1(data))
    print(part2(data))

