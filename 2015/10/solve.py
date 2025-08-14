#!/usr/bin/env python
from functools import cache

test_1 = """1"""
test_2 = """"""


def parse_data(data):
    return data[0]


def iterate(sequence):
    c = sequence[0]
    count = 1
    result = ''
    for new_c in sequence[1:]:
        if new_c == c:
            count += 1
        else:
            result += str(count) + c
            count = 1
            c = new_c

    return result + str(count) + c


def part1(data, iters=40):
    sequence = parse_data(data)

    for i in range(0, iters):
        sequence = iterate(sequence)

    return len(sequence)


def part2(data):
    return part1(data, iters=50)


if __name__ == '__main__':

    assert part1(test_1, 5) == 6

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

