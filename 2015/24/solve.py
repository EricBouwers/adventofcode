#!/usr/bin/env python
from functools import reduce
from itertools import permutations, combinations, product
from operator import mul

test_1 = """1
2
3
4
5
7
8
9
10
11
"""
test_2 = """"""


def parse_data(data):
    return [int(x) for x in data]


def part1(data, groups=3):
    packages = parse_data(data)
    total_sum = sum(packages)
    wanted_sum = total_sum / groups

    smallest_i = 1
    found_distribution = False
    smallest_quantum = 1000000000000000000000000
    while not found_distribution:
        for p in combinations(packages, smallest_i):
            if sum(p) == wanted_sum:
                smallest_quantum = min(smallest_quantum, reduce(mul, p, 1))
                found_distribution = True
        smallest_i += 1

    return smallest_quantum


def part2(data):
    return part1(data, 4)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 99
    assert part2(test_1.splitlines()) == 44

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

