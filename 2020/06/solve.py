#!/usr/bin/env python
import string
from functools import reduce
from operator import add

test_1 = """abcx
abcy
abcz"""
test_2 = """abc

a
b
c

ab
ac

a
a
a
a

b"""
test_3 = """"""
test_4 = """"""


def parse_groups(data):
    groups = []
    group = []
    for line in data:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
    groups.append(group)
    return groups


def part1(data):
    groups = parse_groups(data)
    return reduce(add, [len(set("".join(g))) for g in groups])


def part2(data):
    groups = parse_groups(data)
    return reduce(add, [
        len(set(string.ascii_lowercase).intersection(*[set(p) for p in g])) for g in groups
    ])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 6
    assert part1(test_2.splitlines()) == 11
    assert part2(test_2.splitlines()) == 6

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

