#!/usr/bin/env python

import sys


def part1(data):
    return None


def part2(data):
    return None


if __name__ == '__main__':

    assert part1("") == None
    assert part2("") == None

    with open(sys.argv[1]) as f:
        data = f.readlines()

    print(part1(data))
    print(part2(data))

