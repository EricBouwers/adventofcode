#!/usr/bin/env python
import operator

test_1 = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
test_2 = """"""


def parse_data(data):
    return [[int(v) for v in l.split()] for l in data]


def is_safe(report):
    return (all([-4 < x < 0 for x in map(lambda x: operator.sub(*x), zip(report, report[1:]))]) or
            all([0 < x < 4 for x in map(lambda x: operator.sub(*x), zip(report, report[1:]))]))


def part1(data):
    return sum(map(is_safe, parse_data(data)))


def part2(data):
    count = 0
    for report in parse_data(data):
        safe = is_safe(report)
        i = 0
        while not safe and i < len(report):
            safe = is_safe([x for idx, x in enumerate(report) if idx != i])
            i += 1
        count += 1 if safe else 0

    return count


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 2
    assert part2(test_1.splitlines()) == 4

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))