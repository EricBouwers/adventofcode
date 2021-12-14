#!/usr/bin/env python
from collections import defaultdict

test_1 = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_input(data):
    start = data[0]
    transitions = {}
    for transition in data[2:]:
        t = transition.split(" -> ")
        transitions[(t[0][0], t[0][1])] = t[1]
    return start, transitions


def part1(data, iterations=10):
    start, transitions = parse_input(data)

    polymer = defaultdict(lambda: 0)
    pairs = zip(start, start[1:])
    for p in pairs:
        polymer[p] += 1

    for i in range(0, iterations):
        new_poly = defaultdict(lambda:0)
        for p in polymer:
            new_char = transitions[p]
            new_poly[(p[0], new_char)] += polymer[p]
            new_poly[(new_char, p[1])] += polymer[p]
        polymer = new_poly

    chars = defaultdict(lambda: 0)
    for p, i in polymer.items():
        chars[p[0]] += i
    chars[start[-1]] += 1

    return max(chars.values()) - min(chars.values())


def part2(data):
    return part1(data, iterations=40)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 1588
    assert part2(test_1.splitlines()) == 2188189693529

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

