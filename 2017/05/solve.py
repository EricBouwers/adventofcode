#!/usr/bin/env python

import sys

def count_steps(instructions, offset_func):
    index = 0
    steps = 0

    while len(instructions) > index >= 0:
        jump = instructions[index]
        instructions[index] += offset_func(instructions[index])
        index += jump
        steps += 1

    print instructions
    return steps

def always_one(x):
    return 1

def inc_or_dec(x):
    return 1 if x < 3 else -1

if __name__ == '__main__':
    assert count_steps([0, 3, 0, 1, -3], always_one) == 5
    assert count_steps([0, 3, 0, 1, -3], inc_or_dec) == 10

    jumps = [int(x) for x in sys.argv[1].split()]
    print count_steps(jumps, always_one)
    jumps = [int(x) for x in sys.argv[1].split()]
    print count_steps(jumps, inc_or_dec)

