#!/usr/bin/env python

import sys

from int_code_comp import intcode_comp

test_1 = """"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def run_acsii_program(data, main):
    memory = [int(x) for x in data.split(",")]
    pointer = 0
    relative_pointer = 0
    finished = False
    output = {}
    cur_pos = (0, 0)

    args = [ord(c) for c in main]
    max_x = 0

    return_val = None

    while not finished:
        memory, pointer, s, relative_pointer = intcode_comp(memory, args, True, pointer, relative_pointer)

        if s is None:
            finished = True
        else:
            if s != 10:
                output[cur_pos] = str(chr(s)) if s < 1000 else str(s)

            if s == 10:
                max_x = max(max_x, cur_pos[0])
                cur_pos = (0, cur_pos[1] + 1)
            else:
                cur_pos = (cur_pos[0] + 1, cur_pos[1])
                return_val = s

    print_output(output, max_x, cur_pos[1])
    return return_val


def print_output(output, max_x, max_y):
    for y in range(max_y):
        if (0, y) in output:
            line = ""
            for x in range(max_x):
                line += output.get((x, y), " ")
            print(line)
        else:
            print("\n")


def part1(data):
    main = "NOT C T\nAND D T\nNOT A J\nOR T J\nWALK\n"
    result = run_acsii_program(data, main)

    return result


def part2(data):
    main = "NOT C T\nAND D T\nAND H T\nNOT A J\nOR T J\nNOT B T\nAND D T\nOR T J\nRUN\n"
    result = run_acsii_program(data, main)

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

