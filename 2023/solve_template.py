#!/usr/bin/env python

test_1 = """"""
test_2 = """"""


def parse_data(data):
    return data


def part1(data):
    parsed = parse_data(data)
    print(parsed)
    return None


def part2(data):
    parsed = parse_data(data)
    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == None
    assert part2(test_1.splitlines()) == None

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

