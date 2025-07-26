#!/usr/bin/env python
import re

test_1 = """""
"abc"
"aaa\\"aaa"
"\\x27"
"""
test_2 = """"""


def parse_data(data):
    return data


def mem_len(s):
    return len(eval(s))


def exp_len(s):
    return len('"' + re.escape(s).replace('"', '\\"') + '"')


def part1(data):
    lines = parse_data(data)
    return sum(map(len, lines)) - sum(map(mem_len, lines))


def part2(data):
    lines = parse_data(data)
    return sum(map(exp_len, lines)) - sum(map(len, lines))


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 12
    assert part2(test_1.splitlines()) == 19

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

