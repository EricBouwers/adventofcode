#!/usr/bin/env python

test_1 = """2199943210
3987894921
9856789892
8767896789
9899965678"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_map(m):
    lava_map = {}
    for y, l in enumerate(m):
        for x, v in enumerate(l):
            lava_map[(y, x)] = int(v)

    return lava_map


def neighbours(c):
    return [
        (c[0], c[1] - 1),
        (c[0], c[1] + 1),
        (c[0] - 1, c[1]),
        (c[0] + 1, c[1]),
    ]


def low_points(lava_map):
    return [
        c for c in lava_map.keys()
        if sum([(n not in lava_map or lava_map[n] > lava_map[c]) for n in neighbours(c)]) == 4
    ]


def find_basin(c, lava_map):
    basin = []
    to_inspect = {c}
    while len(to_inspect) is not 0:
        c = to_inspect.pop()
        basin.append(c)
        for n in neighbours(c):
            if n in lava_map and lava_map[n] != 9 and n not in basin:
                to_inspect.add(n)

    return basin


def part1(data):
    lava_map = parse_map(data)
    risk = sum([lava_map[l] + 1 for l in low_points(lava_map)])
    return risk


def part2(data):
    lava_map = parse_map(data)
    basins = [find_basin(l, lava_map) for l in low_points(lava_map)]
    basins = sorted(basins, key=len, reverse=True)

    return len(basins[0]) * len(basins[1]) * len(basins[2])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 15
    assert part2(test_1.splitlines()) == 1134

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

