#!/usr/bin/env python

test_1 = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
test_2 = """
1-10
1-2

1
"""


def parse_data(data):
    ranges = []
    ingredients = []

    for d in data:
        if "-" in d:
            ranges.append((list(map(int, d.split("-")))))
        elif d:
            ingredients.append(int(d))

    return ranges, ingredients


def part1(data):
    ranges, ingredients = parse_data(data)

    total = 0
    for i in ingredients:
        match = False
        for r in ranges:
            match = match or r[0] <= i <= r[1]
        total += 1 if match else 0

    return total


def part2(data):
    ranges, _ = parse_data(data)
    ranges = sorted(ranges, key=lambda r:r[0])

    total = 0
    cur_from, cur_to = ranges[0]
    for f,t in ranges[1:]:
        if cur_to < f:
            total += cur_to - cur_from + 1
            cur_to = t
            cur_from = f
        else:
            cur_to = max(cur_to, t)
    total += cur_to - cur_from + 1

    return total


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 3
    assert part2(test_1.splitlines()) == 14
    assert part2(test_2.splitlines()) == 10

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
