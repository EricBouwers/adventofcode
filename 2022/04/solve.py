#!/usr/bin/env python

test_1 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
test_2 = """"""


def parse_data(data):
    pairs = []
    for d in data:
        pairs.append([
            [int(d.split(",")[0].split("-")[0]), int(d.split(",")[0].split("-")[1])],
            [int(d.split(",")[1].split("-")[0]), int(d.split(",")[1].split("-")[1])]
        ])
    return pairs


def is_contained(p):
    return (p[0][0] >= p[1][0] and p[0][1] <= p[1][1]) or (p[0][0] <= p[1][0] and p[0][1] >= p[1][1])


def part1(data):
    pairs = parse_data(data)
    return sum(map(is_contained, pairs))


def overlaps(p):
    set1 = set(range(p[0][0], p[0][1]+1))
    set2 = set(range(p[1][0], p[1][1]+1))
    return not set1.isdisjoint(set2)


def part2(data):
    pairs = parse_data(data)
    print([x for x in map(overlaps, pairs)])
    return sum(map(overlaps, pairs))


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 2
    assert part2(test_1.splitlines()) == 4

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

