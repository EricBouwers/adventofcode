#!/usr/bin/env python

import sys
from itertools import permutations

import int_code_comp

test_1 = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
test_2 = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
test_3 = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
test_4 = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
test_5 = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"


def part1(data):

    max_signal = 0
    for sequence in permutations([0, 1, 2, 3, 4], 5):
        signal = 0
        for p in sequence:
            memory = [int(x) for x in data.split(",")]
            args = [p, signal]
            signal = int_code_comp.intcode_comp(memory, args, True)[2]
        max_signal = max(max_signal, signal)

    return max_signal


def has_finished(comp):
    return comp[0][comp[1]] == 99


def loop_over_comps(comps, signal):
    new_comps = []
    for memory, pointer, args in comps:
        args.append(signal)
        memory, pointer, new_signal = int_code_comp.intcode_comp(memory, args, True, pointer)
        new_comps.append((memory, pointer, args))

        if new_signal is not None:
            signal = new_signal
    return signal, new_comps


def part2(data):
    max_signal = 0
    for sequence in permutations([5, 6, 7, 8, 9], 5):
        comps = [
            ([int(x) for x in data.split(",")], 0, [s])
            for s in sequence
        ]

        signal = 0
        while not has_finished(comps[-1]):
            signal, comps = loop_over_comps(comps, signal)

        max_signal = max(max_signal, signal)
    return max_signal


if __name__ == '__main__':

    assert part1(test_1) == 43210
    assert part1(test_2) == 54321
    assert part1(test_3) == 65210
    assert part2(test_4) == 139629729
    assert part2(test_5) == 18216

    with open(sys.argv[1]) as f:
        data = f.readlines()

    print(part1(data[0]))
    print(part2(data[0]))

