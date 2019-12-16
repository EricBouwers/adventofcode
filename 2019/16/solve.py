#!/usr/bin/env python
import datetime
import numpy as np
from _operator import mul

test_1 = """12345678"""
test_2 = """80871224585914546619083218645595"""
test_3 = """03036732577212944063491565474664"""
test_4 = """02935109699940807407585447034323"""

PHASE_DICT = {}


def get_pattern(i, length):

    if (i, length) not in PHASE_DICT:
        p = []
        pattern_numbers = [0, 1, 0, -1]
        count_length = length
        while count_length > -1:
            pattern_number = pattern_numbers.pop(0)
            p += i * [pattern_number]
            pattern_numbers.append(pattern_number)
            count_length -= i

        PHASE_DICT[(i, length)] = np.array(p[1:length+1])

    return PHASE_DICT[(i, length)]


def part1(data, phases):
    signal = [int(x) for x in data]
    len_signal = len(signal)

    signal = run_fft_phases(len_signal, phases, signal)

    return signal


def run_fft_phases(len_signal, phases, signal):

    signal = np.array(signal)
    while phases > 0:
        new_signal = []
        for i, x in enumerate(signal):
            new_signal.append(
                abs((signal * get_pattern(i + 1, len_signal)).sum()) % 10)

        signal = new_signal
        phases -= 1

    return signal


def part2(data):
    signal = [int(x) for x in data] * 10000
    len_signal = len(signal)

    to_skip = int("".join(map(str, signal[0:7])))
    signal = run_fft_phases(len_signal, 100, signal)

    return signal[to_skip:to_skip+8]


if __name__ == '__main__':

    assert part1(test_1, 1) == [4, 8, 2, 2, 6, 1, 5, 8]
    assert part1(test_1, 2) == [3, 4, 0, 4, 0, 4, 3, 8]
    assert part1(test_1, 4) == [0, 1, 0, 2, 9, 4, 9, 8]
    assert part1(test_2, 100)[0:8] == [2, 4, 1, 7, 6, 1, 7, 6]
    print("done testing part 1")

    assert part2(test_3) == 84462026
    # assert part2(test_4) == 78725270

    print("done testing")

    with open('input') as f:
        data = f.read()

    print(datetime.datetime.now())
    print(part1(data, 100)[0:8])
    print(datetime.datetime.now())
    print(part2(data))
    print(datetime.datetime.now())
