#!/usr/bin/env python
from itertools import permutations

test_1 = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
test_2 = """"""


def parse_data(data):
    steps = {}
    all_cities = set()
    for line in data:
        f, t = line.split(' to ')
        t, km = t.split(' = ')
        steps[(f, t)] = int(km)
        steps[(t, f)] = int(km)
        all_cities.add(f)
        all_cities.add(t)

    return steps, all_cities


def find_path(f, steps, all_cities):
    return f(sum([steps[(f, t)] for f, t in zip(path, path[1:])]) for path in permutations(all_cities))

def part1(data):
    steps, all_cities = parse_data(data)
    return find_path(min, steps, all_cities)


def part2(data):
    steps, all_cities = parse_data(data)
    return find_path(max, steps, all_cities)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 605
    assert part2(test_1.splitlines()) == 982

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

