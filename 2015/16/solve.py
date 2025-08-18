#!/usr/bin/env python
from collections import defaultdict

test_1 = """Sue 1: cars: 9, akitas: 3, goldfish: 0
Sue 5: cars: 2, akitas: 0, goldfish: 5
Sue 107: cars: 2, trees: 6, goldfish: 4
"""
test_2 = """"""

ticker_tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

def parse_data(data):
    sues = {}
    for line in data:
        sue_props = {}
        parts = line.replace(',','').replace(':','').split(" ")
        sue_nr = int(parts[1])
        for i in range(2, len(parts), 2):
            sue_props[parts[i]] = int(parts[i+1])
        sues[sue_nr] = sue_props
    return sues

def exact_match(partial, full):
    match = True
    for p, v in partial.items():
        match = match and full[p] == v
    return match

def range_match(partial, full):
    match = True
    for p, v in partial.items():
        if p in ['cats', 'trees']:
            match = match and full[p] < v
        elif p in ['pomeranians', 'goldfish']:
            match = match and full[p] > v
        else:
            match = match and full[p] == v
    return match


def part1(data):
    sue_props = parse_data(data)

    for nr, props in sue_props.items():
        if exact_match(props, ticker_tape):
            return nr


def part2(data):
    sue_props = parse_data(data)

    for nr, props in sue_props.items():
        if range_match(props, ticker_tape):
            return nr


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 5
    assert part2(test_1.splitlines()) == 107

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

