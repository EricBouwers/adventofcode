#!/usr/bin/env python
import operator
from collections import Counter

test_1 = """3   4
4   3
2   5
1   3
3   9
3   3
"""
test_2 = """"""


def parse_data(data):
    l1, l2 = [], []
    for l in data:
        left, right = [int(x) for x in l.split('  ')]
        l1.append(left)
        l2.append(right)
    return l1, l2


def part1(data):
    l1, l2 = parse_data(data)
    l1 = sorted(l1)
    l2 = sorted(l2)
    return sum(map(lambda x: abs(operator.sub(*x)), zip(l1, l2)))


def part2(data):
    l1, l2 = parse_data(data)
    l2_count = Counter(l2)

    return sum(map(lambda x: l2_count.get(x, 0) * x, l1))


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 11
    assert part2(test_1.splitlines()) == 31

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

