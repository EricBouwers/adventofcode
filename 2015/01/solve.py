#!/usr/bin/env python

test_1 = """(()(()("""
test_2 = """)())())"""
test_3 = """()())"""


def parse_data(data):
    return data[0]


def part1(data):
    presses = parse_data(data)
    return presses.count('(') - presses.count(')')


def part2(data):
    presses = parse_data(data)
    floor = 0
    for i,p in enumerate(presses):
        floor += 1 if p == '(' else -1
        if floor == -1:
            return i + 1


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 3
    assert part1(test_2.splitlines()) == -3
    assert part2(test_1.splitlines()) == None

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

