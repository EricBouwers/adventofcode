#!/usr/bin/env python
from collections import defaultdict
from itertools import permutations

test_1 = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""
test_2 = """"""


def parse_data(data):
    changes = defaultdict(lambda: 0)
    relatives = set()
    for line in data:
        parts = line.split(" ")
        changes[(parts[0], parts[-1][0:-1])] = int(parts[3]) * (1 if parts[2] == 'gain' else -1)
        relatives.add(parts[0])

    return changes, relatives

def calculate_changes(seating, changes):
    return sum([changes[(a, b)] + changes[(b, a)] for a, b in zip(seating, seating[1:] + seating[0:1])])

def part1(data):
    changes, relatives = parse_data(data)
    return max([calculate_changes(p, changes) for p in permutations(relatives)])


def part2(data):
    changes, relatives = parse_data(data)
    relatives.add('me')
    return max([calculate_changes(p, changes) for p in permutations(relatives)])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 330

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

