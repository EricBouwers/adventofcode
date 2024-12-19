#!/usr/bin/env python
import re
from functools import cache

test_1 = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""
test_2 = """"""


def parse_data(data):
    towels = []
    designs = []
    for d in data:
        if ',' in d:
            towels = d.split(", ")
        elif d:
            designs.append(d)

    return towels, designs


@cache
def get_all_matches(design, towels):
    if design == "":
        return 1
    else:
        return sum([
            get_all_matches(design[len(t):], towels) for t in towels if design.startswith(t)
        ])


def part1(data):
    towels, designs = parse_data(data)

    pattern = re.compile("^(" + "|".join(towels) + ")+$")
    return len([d for d in designs if re.match(pattern, d)])


def part2(data):
    towels, designs = parse_data(data)

    return sum([get_all_matches(d, tuple(towels)) for d in designs])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 6
    assert part2(test_1.splitlines()) == 16

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

