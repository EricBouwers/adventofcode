#!/usr/bin/env python
import re
from collections import defaultdict
from functools import reduce
from operator import mul, add

test_1 = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""
test_2 = """"""


def parse_data1(data):
    spaces = re.compile("\\s+")
    problems = defaultdict(list)
    operations = []
    for d in data:
        if "*" in d:
            operations = [mul if o == "*" else add for o in re.split(spaces, d.strip())]
        else:
            for i, num in enumerate(re.split(spaces, d.strip())):
                problems[i].append(int(num))

    return problems, operations


def parse_block(block):
    numbers = []
    for i in range(0, len(block[0])):
        number = ""
        for b in block:
            number += b[i] if b[i] else ''
        numbers.append(number)

    return [int(n.strip()) for n in numbers if n.strip()]

def parse_data2(data):
    spaces = re.compile("\\s+")
    non_spaces = re.compile("[^\\s]")

    operation_line = data[-1]
    operations = [mul if o == "*" else add for o in re.split(spaces, operation_line.strip())]
    lengths = [len(l) + 1 for l in re.split(non_spaces, operation_line)[1:]]

    number_lines = data[0:len(data)-1]
    problems = defaultdict(list)

    seen = 0
    for i,l in enumerate(lengths):
        problems[i] = parse_block([n[seen:seen+l] for n in number_lines])
        seen += l

    return problems, operations


def part1(data):
    problems, operations = parse_data1(data)

    totals = 0
    for i, p in problems.items():
        totals += reduce(operations[i], p)

    return totals


def part2(data):
    problems, operations = parse_data2(data)

    totals = 0
    for i, p in problems.items():
        totals += reduce(operations[i], p)

    return totals


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 4277556
    assert part2(test_1.splitlines()) == 3263827

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
