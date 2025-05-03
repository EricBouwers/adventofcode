#!/usr/bin/env python
from hashlib import md5

test_1 = """abcdef"""
test_2 = """"""


def parse_data(data):
    return data[0]


def part1(data):
    prefix = parse_data(data)

    count = 0
    while True:
        hash = md5((prefix + str(count)).encode("utf-8")).hexdigest()
        if hash.startswith('00000'):
            return count
        else:
            count += 1


def part2(data):
    prefix = parse_data(data)

    count = 0
    while True:
        hash = md5((prefix + str(count)).encode("utf-8")).hexdigest()
        if hash.startswith('000000'):
            return count
        else:
            count += 1



if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 609043

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

