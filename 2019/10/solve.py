#!/usr/bin/env python
import math
from collections import defaultdict

test_1 = """.#..#
.....
#####
....#
...##"""
test_2 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""
test_3 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""


def parse_astroids(data):
    astroids = []
    y = 0
    for d in data:
        x = 0
        for c in d:
            if c == "#":
                astroids.append((x, y))
            x += 1
        y += 1
    return astroids


def is_between(o, a, c):
    dxc = o[0] - a[0]
    dyc = o[1] - a[1]
    dxl = c[0] - a[0]
    dyl = c[1] - a[1]

    cross = dxc * dyl - dyc * dxl
    if cross != 0:
        return False

    if abs(dxl) >= abs(dyl):
        return a[0] <= o[0] <= c[0] if dxl > 0 else c[0] <= o[0] <= a[0]
    else:
        return a[1] <= o[1] <= c[1] if dyl > 0 else c[1] <= o[1] <= a[1]


def no_one_in_between(a, c, astroids):
    for o in astroids:
        if o not in [a, c] and is_between(o, a, c):
            return False
    return True


def part1(data):
    astroids = parse_astroids(data)
    visibles = extract_visibles(astroids)

    max_visible = 0
    max_c = None
    for c, v in visibles.items():
        if len(v) > max_visible:
            max_c = c
            max_visible = len(v)

    return max_c, astroids, visibles, max_visible


def extract_visibles(astroids, interested_in=None):
    if interested_in is None:
        interested_in = astroids

    new_astroids = {x:x for x in astroids}
    visibles = defaultdict(list)
    for a in interested_in:
        del new_astroids[a]
        for c in new_astroids.keys():
            if a != c and no_one_in_between(a, c, astroids):
                visibles[a].append(c)
                visibles[c].append(a)
    return visibles


def dotproduct(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))


def length(v):
    return math.sqrt(dotproduct(v, v))


def angle(v1, v2):
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))


def calc_angle(station, x):
    new_x = (x[0]-station[0], x[1]-station[1])
    return angle((0, -1), new_x) if x[0] >= station[0] else 360 - angle((0, -1), new_x)


def part2(data, up_to):
    station, astroids, visibles, max_visible = part1(data)
    blasted_ones = []

    while len(blasted_ones) < up_to:
        newly_blasted = visibles[station]

        newly_blasted.sort(key=lambda x: calc_angle(station, x), reverse=False)

        blasted_ones = blasted_ones + newly_blasted
        astroids = set(astroids) - set(newly_blasted)
        visibles = extract_visibles(astroids, [station])

    return blasted_ones[up_to-1][0] * 100 + blasted_ones[up_to-1][1]


if __name__ == '__main__':

    assert part1(test_1.splitlines())[0] == (3, 4)
    assert part1(test_2.splitlines())[0] == (5, 8)
    assert part2(test_3.splitlines(), 1) == 1112
    assert part2(test_3.splitlines(), 2) == 1201
    assert part2(test_3.splitlines(), 100) == 1016
    assert part2(test_3.splitlines(), 200) == 802

    with open('input') as f:
        data = f.readlines()

    print(part1(data)[3])
    print(part2(data, 200))

