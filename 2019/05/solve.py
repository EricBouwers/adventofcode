#!/usr/bin/env python

import sys
from _operator import add, mul

test_1 = "3,0,4,0,99"

OPERATORS = {
    1: lambda modes, mem, p, _: simple_ops(add, modes, mem, p),
    2: lambda modes, mem, p, _: simple_ops(mul, modes, mem, p),
    3: lambda modes, mem, p, args: set_val(modes, mem, p, args),
    4: lambda modes, mem, p, _: print_val(modes, mem, p),
    5: lambda modes, mem, p, _: jump_true(modes, mem, p),
    6: lambda modes, mem, p, _: jump_false(modes, mem, p),
    7: lambda modes, mem, p, _: simple_ops(less_than, modes, mem, p),
    8: lambda modes, mem, p, _: simple_ops(equals_to, modes, mem, p)
}


def less_than(x, y):
    return 1 if x < y else 0


def equals_to(x, y):
    return 1 if x == y else 0


def set_val(_, mem, p, args):
    mem[mem[p+1]] = args[0]
    p += 2
    return mem, p


def print_val(modes, mem, p):
    val = _get_mem_val(modes, mem, p, 0)
    print(val)
    p += 2
    return mem, p


def simple_ops(op, modes, mem, p):
    val_1 = _get_mem_val(modes, mem, p, 0)
    val_2 = _get_mem_val(modes, mem, p, 1)
    mem[mem[p + 3]] = op(val_1, val_2)
    p += 4
    return mem, p


def jump_true(modes, mem, p):
    val1 = _get_mem_val(modes, mem, p, 0)
    val2 = _get_mem_val(modes, mem, p, 1)
    if val1 != 0:
        return mem, val2
    else:
        p += 3
        return mem, p


def jump_false(modes, mem, p):
    val1 = _get_mem_val(modes, mem, p, 0)
    val2 = _get_mem_val(modes, mem, p, 1)
    if val1 == 0:
        return mem, val2
    else:
        p += 3
        return mem, p


def parse_op_and_modes(cur_val):
    parsed = []
    cur_val, op = divmod(cur_val, 100)
    parsed.append(op)

    while cur_val:
        cur_val, mode = divmod(cur_val, 10)
        parsed.append(mode)

    return parsed


def _get_mem_val(modes, mem, p, i):
    if len(modes) > i and modes[i] == 1:
        return mem[p + 1 + i]
    else:
        return mem[mem[p + 1 + i]]


def intcode_comp(memory, args):
    pointer = 0
    max_p = len(memory)
    while pointer < max_p:
        cur_val = memory[pointer]
        op_and_modes = parse_op_and_modes(cur_val)

        if op_and_modes[0] == 99:
            return memory

        op = OPERATORS[op_and_modes[0]]
        memory, pointer = op(op_and_modes[1:], memory, pointer, args)


def part1(data):
    inputs = [int(x) for x in data.split(",")]
    return intcode_comp(inputs, [1])


def part2(data):
    inputs = [int(x) for x in data.split(",")]
    return intcode_comp(inputs, [5])


if __name__ == '__main__':

    assert part1(test_1) == [1, 0, 4, 0, 99]
    assert part2(test_1) == [5, 0, 4, 0, 99]

    intcode_comp([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [0])
    intcode_comp([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [5])

    print("tests done \n\n\n")

    with open(sys.argv[1]) as f:
        data = f.readlines()

    part1(data[0])
    part2(data[0])

