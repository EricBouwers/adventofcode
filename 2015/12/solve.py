#!/usr/bin/env python
import json
import re

test_1 = """{"a":{"b":4},"c":-1}"""
test_2 = """[1,{"c":"red","b":2},3]"""
test_3 = """[{"d":"red","e":[1,2,3,4],"f":5}]"""


def parse_data(data):
    return data[0]


def count_structure(structure):
    if isinstance(structure, int):
        return structure
    elif isinstance(structure, list):
        return sum([count_structure(s) for s in structure])
    elif isinstance(structure, dict):
        if 'red' in structure.values():
            return 0
        else:
            return sum([count_structure(s) for s in structure.values()])
    else:
        return 0


def part1(data):
    parsed = parse_data(data)
    nums = re.findall(r'-?\d+', parsed)
    return sum([int(n) for n in nums])


def part2(data):
    parsed = parse_data(data)
    structure = json.loads(parsed)

    return count_structure(structure)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 3
    assert part2(test_2.splitlines()) == 4
    assert part2(test_3.splitlines()) == 0

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

