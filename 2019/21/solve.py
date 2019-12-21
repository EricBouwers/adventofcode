#!/usr/bin/env python

import sys

from int_code_comp import intcode_comp

test_1 = """"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def run_line(memory, pointer, relative_pointer, args):
    output = ""
    s = 0
    while s != 10:
        memory, pointer, s, relative_pointer = intcode_comp(memory, args, True, pointer, relative_pointer)
        if s > 1000:
            return s, memory, pointer, relative_pointer
        output += str(chr(s))

    return output, memory, pointer, relative_pointer


def parse_world(data, args, stepping="Walking...\n"):
    memory = [int(x) for x in data.split(",")]
    pointer = 0
    relative_pointer = 0
    finished = False
    world = {}
    cur_pos = (0, 0)

    output, memory, pointer, relative_pointer = run_line(memory, pointer, relative_pointer, [])

    output = stepping
    while output == stepping:
        memory, pointer, s, relative_pointer = intcode_comp(memory, args, True, pointer, relative_pointer)
        output, memory, pointer, relative_pointer = run_line(memory, pointer, relative_pointer, args)

    if isinstance(output, int):
        return world, output

    memory, pointer, s, relative_pointer = intcode_comp(memory, args, True, pointer, relative_pointer)
    output, memory, pointer, relative_pointer = run_line(memory, pointer, relative_pointer, args)

    while not finished:
        memory, pointer, s, relative_pointer = intcode_comp(memory, args, True, pointer, relative_pointer)

        if s is None:
            finished = True
        else:
            if s != 10:
                world[cur_pos] = str(chr(s))

            if s == 10:
                cur_pos = (0, cur_pos[1] + 1)
            else:
                cur_pos = (cur_pos[0] + 1, cur_pos[1])

    return world, None


def print_world(world):
    max_x, max_y = 0, 0
    for k in world:
        max_x, max_y = max(max_x, k[0]), max(max_y, k[1])

    for y in range(max_y):

        if (0, y) in world:
            line = ""
            for x in range(max_x):
                line += world[(x, y)]
            print(line)
        else:
            print("\n")


def part1(data):
    main = "NOT C T\nAND D T\nNOT A J\nOR T J\nWALK\n"
    args = [ord(c) for c in main]

    world, result = parse_world(data, args)

    if world is not None:
        print_world(world)

    return result


def part2(data):
    main = "NOT C T\nAND D T\nAND H T\nNOT A J\nOR T J\nNOT B T\nAND D T\nOR T J\nRUN\n"
    args = [ord(c) for c in main]

    world, result = parse_world(data, args, "Running...\n")

    if world is not None:
        print_world(world)

    return result


if __name__ == '__main__':

    # assert part1(test_1) == None
    # assert part1(test_2) == None
    # assert part2(test_3) == None
    # assert part2(test_4) == None

    with open('input') as f:
        data = f.read()

    print(part1(data))
    print(part2(data))

