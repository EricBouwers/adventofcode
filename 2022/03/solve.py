#!/usr/bin/env python

test_1 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
test_2 = """"""


def to_val(c):
    return ord(c) - 96 if ord(c) >= 97 else ord(c) - 38


def part1(data):
    total = 0
    for sack in data:
        common = list(set(sack[0:int(len(sack)/2)]).intersection(sack[int(len(sack)/2):]))
        total += sum(map(to_val, common))
    return total


def part2(data):
    total = 0
    for i in range(0, len(data), 3):
        common = list(set(data[i]).intersection(data[i+1]).intersection(data[i+2]))
        total += sum(map(to_val, common))
    return total


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 157
    assert part2(test_1.splitlines()) == 70

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

