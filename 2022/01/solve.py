#!/usr/bin/env python
from collections import defaultdict

test_1 = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_data(data):
    elves = defaultdict(lambda: 0)
    elf = 0
    for d in data:
        if d is "":
            elf += 1
        else:
            elves[elf] += int(d)
    return elves


def part1(data):
    return max(parse_data(data).values())


def part2(data):
    return sum(sorted(parse_data(data).values(), reverse=True)[0:3])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 24000
    assert part2(test_1.splitlines()) == 45000

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

