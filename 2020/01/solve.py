#!/usr/bin/env python
from itertools import combinations

test_1 = """1721
979
366
299
675
1456"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data):
    expenses = [int(x) for x in data]
    combos = combinations(expenses, 2)
    for c in combos:
        if sum(c) == 2020:
            return c[0] * c[1]

    return None


def part2(data):
    expenses = [int(x) for x in data]
    combos = combinations(expenses, 3)
    for c in combos:
        if sum(c) == 2020:
            return c[0] * c[1] * c[2]

    return None


if __name__ == '__main__':

    assert part1(test_1.split('\n')) == 514579
    assert part2(test_1.split('\n')) == 241861950

    with open('input') as f:
        data = f.readlines()

    print(part1(data))
    print(part2(data))

