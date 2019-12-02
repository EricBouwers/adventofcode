#!/usr/bin/env python

import sys
from _operator import add, mul

test_1 = "1,9,10,3,2,3,11,0,99,30,40,50"
test_2 = "1,0,0,0,99"
test_3 = "2,3,0,3,99"
test_4 = "2,4,4,5,99,0"
test_5 = "1,1,1,4,99,5,6,0,99"

OPERATORS = {
    1: lambda m, p: simple_ops(add, m, p),
    2: lambda m, p: simple_ops(mul, m, p)
}


def simple_ops(op, mem, p):
    mem[mem[p + 3]] = op(mem[mem[p + 1]], mem[mem[p + 2]])
    p += 4
    return mem, p


def intcode_comp(memory):
    pointer = 0
    max_p = len(memory)
    while pointer < max_p:
        cur_val = memory[pointer]
        if cur_val == 99:
            return memory

        op = OPERATORS[cur_val]
        memory, pointer = op(memory, pointer)


def part1(input_data, index, noun=None, verb=None):
    inputs = [int(x) for x in input_data.split(",")]

    if noun is not None:
        inputs[1] = noun

    if verb is not None:
        inputs[2] = verb

    return intcode_comp(inputs)[index]


def part2(input_data, val):

    for i in range(0, 99):
        for j in range(0, 99):
            output = part1(input_data, 0, noun=i, verb=j)
            if output == val:
                return i, j


if __name__ == '__main__':

    assert part1(test_1, 0) == 3500
    assert part1(test_2, 0) == 2
    assert part1(test_3, 3) == 6
    assert part1(test_4, 5) == 9801
    assert part1(test_5, 0) == 30

    with open(sys.argv[1]) as f:
        data = f.readlines()

    print(part1(data[0], 0, noun=12, verb=2))
    print(part2(data[0], 19690720))
