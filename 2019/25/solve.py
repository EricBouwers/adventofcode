#!/usr/bin/env python
import itertools
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

    args = [ord(c) for c in main]
    cur_line = ""

    while not finished:
        memory, pointer, s, relative_pointer = intcode_comp(memory, args, True, pointer, relative_pointer)

        if s is None:
            finished = True
        else:
            if s == 10:
                print(cur_line)

                if cur_line == "Command?" and len(args) == 0:
                    args = [ord(c) for c in input()] + [10]

                cur_line = ""
            else:
                cur_line += str(chr(s))


def part1():
    tries = []
    inv = ['ornament', 'loom', 'spool of cat6', 'wreath', 'fixed point', 'shell', 'weather machine']
    for i in range(1, len(inv)):
        tries += itertools.combinations(inv, i)

    output = ""
    for t in tries:
        for i in t:
            output += "take " + i + "\n"
            output += "south\n"
        for i in t:
            output += "drop " + i + "\n"

    return output


def part2(data):
    return None


MAIN = """east
take loom
east
take fixed point
north
take spool of cat6
west
take shell
east
north
take weather machine
south
south
west
south
take ornament
west
north
take candy cane
south
east
north
west
north
take wreath
north
east
south
"""


if __name__ == '__main__':

    with open('input') as f:
        data = f.read()

    run_acsii_program(data, MAIN + part1())
    print(part2(data))

