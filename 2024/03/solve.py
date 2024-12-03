#!/usr/bin/env python
import operator
import re

test_1 = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
test_2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


def parse_data(data):
    return re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\))|(don't\(\))|(do\(\))",data)


def eval_mul(mul):
    return operator.mul(*map(int, mul[4:-1].split(','))) if mul != "" else ""


def part1(data):
    muls = parse_data(data)
    return sum([eval_mul(m[0]) for m in muls if m[0] != ""])


def part2(data):
    muls = parse_data(data)
    muls = [(eval_mul(m[0]), m[1] != "", m[2] != "") for m in muls]

    summation = 0
    enabled = True
    for mul in muls:
        if enabled and mul[0] != '':
            summation += mul[0]
        elif enabled and mul[1]:
            enabled = False
        elif not enabled and mul[2]:
            enabled = True

    return summation


if __name__ == '__main__':

    assert part1(test_1) == 161
    assert part2(test_2) == 48

    with open('input') as f:
        data = f.read()

    print(part1(data))
    print(part2(data))

