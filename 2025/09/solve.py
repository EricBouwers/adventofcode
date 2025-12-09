#!/usr/bin/env python
from functools import cmp_to_key
from itertools import combinations

test_1 = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
test_2 = """"""


def parse_data(data):
    return [list(map(int, d.split(","))) for d in data]



def between(p, a, b):
    return a <= p <= b or p <= a and p >= b


def inside(p, points):
    inside_or_on_edge = False
    for i in range(0, len(points)):
        j = i - 1
        A = points[i]
        B = points[j]

        if p[0] == A[0] and p[1] == A[1] or p[0] == B[0] and p[1] == B[1]:
            return True
        if A[1] == B[1] and p[1] == A[1] and between(p[0], A[0], B[0]):
            return True

        if between(p[1], A[1], B[1]):
            if p[1] == A[1] and B[1] >= A[1] or p[1] == B[1] and A[1] >= B[1]:
                continue
            else:
                c = (A[0] - p[0]) * (B[1] - p[1]) - (B[0] - p[0]) * (A[1] - p[1])
                if c == 0:
                    return True
                if (A[1] < B[1]) == (c > 0):
                    inside_or_on_edge = not inside_or_on_edge

    return inside_or_on_edge


def part1(data):
    tiles = parse_data(data)
    return max([
        (abs(t1[0] - t2[0])+1) * (abs(t1[1] - t2[1])+1) for t1, t2 in combinations(tiles, 2)
    ])


def size(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)


def part2(data):
    tiles = parse_data(data)

    to_test = {size(t1, t2):(t1, t2) for t1, t2 in combinations(tiles, 2)}

    for possible_max in sorted(to_test.keys(), reverse=True):
        t1, t2 = to_test[possible_max]

        possible = inside((t1[0], t2[1]), tiles) and inside((t2[0], t1[1]), tiles)
        for x in [t1[0], t2[0]]:
            y = min(t1[1], t2[1])
            y_max = max(t1[1], t2[1])
            while possible and y <= y_max:
                possible = possible and inside((x, y), tiles)
                y += 1

        for y in [t1[1], t2[1]]:
            x = min(t1[0], t2[0])
            x_max = max(t1[0], t2[0])
            while possible and x <= x_max:
                possible = possible and inside((x, y), tiles)
                x += 1

        if possible:
            return possible_max


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 50
    assert part2(test_1.splitlines()) == 24

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
