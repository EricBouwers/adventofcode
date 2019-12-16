#!/usr/bin/env python
import datetime
import math

import numpy as np
from _operator import mul

test_1 = """12345678"""
test_2 = """80871224585914546619083218645595"""
test_3 = """03036732577212944063491565474664"""
test_4 = """02935109699940807407585447034323"""

PHASE_DICT = {}


def get_pattern(i, length):
    global PHASE_DICT

    if (i, length) not in PHASE_DICT:
        pattern_numbers = [[0], [1], [0], [-1]]
        steps = sum([i]*4)
        p = [item for sublist in map(mul, pattern_numbers, [i] * 4) for item in sublist] * (math.ceil(length / steps) + 1)
        # PHASE_DICT[(i, length)] = np.array(p[1:length + 1])
        PHASE_DICT[(i, length)] = p[1:length+1]

    return PHASE_DICT[(i, length)]


def part1(data, phases):
    signal = [int(x) for x in data]
    len_signal = len(signal)

    signal = run_fft_phases(len_signal, phases, signal)

    return signal


def run_fft_phases(len_signal, phases, signal):

    while phases > 0:
        new_signal = []
        for i, x in enumerate(signal):
            new_signal.append(
                abs(sum(map(mul, signal, get_pattern(i + 1, len_signal)))) % 10)

        signal = new_signal
        phases -= 1

    return signal


def part2(data):
    signal = [int(x) for x in data] * 10000
    len_signal = len(signal)

    to_skip = int("".join(map(str, signal[0:7])))

    signal = signal[to_skip:]
    signal.reverse()

    if to_skip > len_signal / 2:
        phases = 100
        while phases > 0:
            new_signal = []
            prev_x = None
            for x in signal:
                new_x = x if not prev_x else (prev_x + x) % 10
                new_signal.append(new_x)
                prev_x = new_x

            phases -= 1
            signal = new_signal
    else:
        print("shit")

    signal.reverse()
    return signal[0:8]


if __name__ == '__main__':

    assert part1(test_1, 1) == [4, 8, 2, 2, 6, 1, 5, 8]
    assert part1(test_1, 2) == [3, 4, 0, 4, 0, 4, 3, 8]
    assert part1(test_1, 4) == [0, 1, 0, 2, 9, 4, 9, 8]
    assert part1(test_2, 100)[0:8] == [2, 4, 1, 7, 6, 1, 7, 6]
    print("done testing part 1")

    assert part2(test_3) == [8, 4, 4, 6, 2, 0, 2, 6]
    assert part2(test_4) == [7, 8, 7, 2, 5, 2, 7, 0]

    print("done testing")

    with open('input') as f:
        data = f.read()

    print(datetime.datetime.now())
    print(part1(data, 100)[0:8])
    print(datetime.datetime.now())
    print("".join(map(str, part2(data))))
    print(datetime.datetime.now())
