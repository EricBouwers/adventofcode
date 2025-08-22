#!/usr/bin/env python
from itertools import permutations, combinations

test_1 = """20
15
10
5
5
"""
test_2 = """"""


def parse_data(data):
    return [int(l) for l in data]

def part1(data, eggnog=150):
    containers = parse_data(data)

    return len([
        config for r in range(1, len(containers)) for config in combinations(containers, r) if sum(config) == eggnog
    ])


def part2(data, eggnog=150):
    containers = parse_data(data)

    for r in range(1, len(containers)):
        possibilities = len([config for config in combinations(containers, r) if sum(config) == eggnog])
        if possibilities > 0:
            return possibilities


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 25) == 4
    assert part2(test_1.splitlines(), 25) == 3

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

