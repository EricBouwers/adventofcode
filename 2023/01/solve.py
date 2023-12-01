#!/usr/bin/env python
import re

test_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
test_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def part1(data):
    digits = [[y for y in x if y.isdigit()] for x in data]
    return sum([int(d[0] + d[-1]) for d in digits])


replacements = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def replace_all(s, replacements):
    pattern = '(?=(' + '|'.join(replacements.keys()) + '))'
    sn = re.sub(pattern, lambda x: replacements[x.group(1)], s)
    return sn


def part2(data):
    replaced_data = [replace_all(d, replacements) for d in data]
    return part1(replaced_data)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 142
    assert part2(test_2.splitlines()) == 281

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

