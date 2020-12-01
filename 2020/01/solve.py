#!/usr/bin/env python
from functools import reduce
from itertools import combinations
from operator import mul

test_1 = """1721
979
366
299
675
1456"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def expense_in_parts(data, parts):
    expenses = [int(x) for x in data]
    for c in combinations(expenses, parts):
        if sum(c) == 2020:
            return reduce(mul, c)

    return None


def part1(data):
    return expense_in_parts(data, 2)


def part2(data):
    return expense_in_parts(data, 3)


if __name__ == '__main__':

    assert part1(test_1.split('\n')) == 514579
    assert part2(test_1.split('\n')) == 241861950

    with open('input') as f:
        data = f.readlines()

    print(part1(data))
    print(part2(data))

