#!/usr/bin/env python

import sys

from int_code_comp import intcode_comp

test_1 = """"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data):
    memory = [int(x) for x in data.split(",")]
    pointer = 0
    relative_pointer = 0

    world = {}
    done = False

    while not done:
        memory, pointer, x, relative_pointer = intcode_comp(memory, [], True, pointer, relative_pointer)
        memory, pointer, y, relative_pointer = intcode_comp(memory, [], True, pointer, relative_pointer)
        memory, pointer, what, relative_pointer = intcode_comp(memory, [], True, pointer, relative_pointer)

        done = x is None or y is None or what is None

        if not done:
            world[(x, y)] = what

    blocks = 0
    for k, v in world.items():
        if v == 2:
            blocks = blocks + 1

    return blocks


PAINT_DICT = {
    0: " ",
    1: "#",
    2: "1",
    3: "_",
    4: "*"
}


def print_world(world):
    for y in range(23):
        line = ""
        for x in range(43):
            line += PAINT_DICT[world[(x, y)]]
        print(line)


def part2(data):
    memory = [int(x) for x in data.split(",")]
    pointer = 0
    relative_pointer = 0

    memory[0] = 2

    world = {}
    score = 0
    done = False
    args = [0 for _ in range(10000)] # for part 2 to work make sure you have a very looooooong paddle

    while not done:
        memory, pointer, x, relative_pointer = intcode_comp(memory, args, True, pointer, relative_pointer)
        memory, pointer, y, relative_pointer = intcode_comp(memory, args, True, pointer, relative_pointer)
        memory, pointer, what, relative_pointer = intcode_comp(memory, args, True, pointer, relative_pointer)

        done = x is None or y is None or what is None

        if not done:
            if x == -1 and y == 0:
                score = what
                print(score)
            elif x == 42 and y == 22:
                world[(x, y)] = what
                print_world(world)
                # args = [int(x) for x in input().split(",")]
            else:
                world[(x, y)] = what

    return score


if __name__ == '__main__':

    # assert part1(test_1) == None
    # assert part1(test_2) == None
    # assert part2(test_3) == None
    # assert part2(test_4) == None

    with open('input') as f:
        data = f.readlines()

    print(part1(data[0]))
    print(part2(data[0]))

