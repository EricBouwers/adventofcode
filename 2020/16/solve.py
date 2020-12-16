#!/usr/bin/env python
from collections import defaultdict
from functools import reduce
from operator import add, mul

test_1 = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
test_2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
test_3 = """"""
test_4 = """"""


def parse_input(data):
    ranges = defaultdict(list)
    other_tickets = []

    line = data.pop(0)
    while len(line) > 0:
        parts = line.split(':')
        for r in parts[1].split(' or '):
            ranges[parts[0]].append([int(x) for x in r.split('-')])
        line = data.pop(0)

    data.pop(0)
    my_ticket = [int(x) for x in data.pop(0).split(',')]

    data.pop(0)
    data.pop(0)
    while data:
        other_tickets.append([int(x) for x in data.pop(0).split(',')])

    return ranges, my_ticket, other_tickets


def part1(data):
    ranges, my_ticket, other_tickets = parse_input(data)
    all_ranges = reduce(add, ranges.values())

    invalid_sum = 0
    for t in other_tickets:
        for i in t:
            if sum([r[0] <= i <= r[1] for r in all_ranges]) == 0:
                invalid_sum += i

    return invalid_sum


def is_valid(i, ranges):
    return sum([r[0] <= i <= r[1] for r in ranges]) > 0


def part2(data, fields_of_interest=None):
    ranges, my_ticket, other_tickets = parse_input(data)

    if fields_of_interest is None:
        fields_of_interest = [field for field in ranges.keys() if 'departure' in field]

    all_ranges = reduce(add, ranges.values())
    valid_tickets = []
    for t in other_tickets:
        if sum([sum([r[0] <= i <= r[1] for r in all_ranges]) == 0 for i in t]) == 0:
            valid_tickets.append(t)

    field_index_possibilities = defaultdict(list)
    for i in range(0, len(my_ticket)):
        for field, rs in ranges.items():
            if sum([is_valid(t[i], rs) for t in valid_tickets]) == len(valid_tickets):
                field_index_possibilities[field].append(i)

    field_indexes = {}
    while len(field_indexes) != len(ranges.keys()):
        for field, possibilities in field_index_possibilities.items():
            if len(possibilities) == 1:
                field_indexes[field] = possibilities[0]
        for field in field_index_possibilities:
            field_index_possibilities[field] = [
                x for x in field_index_possibilities[field] if x not in field_indexes.values()
            ]

    return reduce(mul, [my_ticket[field_indexes[field]] for field in fields_of_interest])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 71
    assert part2(test_2.splitlines(), ['class', 'seat']) == 156

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines())) # 1500730351849

