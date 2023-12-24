#!/usr/bin/env python
from itertools import combinations

from sympy import Symbol, solve_poly_system

test_1 = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
test_2 = """"""


def parse_data(data):
    stones = []
    for line in data:
        parts = line.split(" @ ")
        stones.append(
            ([int(x) for x in parts[0].split(', ')], [int(x) for x in parts[1].split(', ')])
        )
    return stones


def get_point(line, steps):
    return [p + steps * v for p, v in zip(line[0], line[1])]


def intersect_in_2d(line1, line2):
    p1 = line1[0][0:2]
    p2 = get_point(line1, 5)[0:2]
    p3 = line2[0][0:2]
    p4 = get_point(line2, 5)[0:2]

    denominator = (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0])
    if denominator == 0:
        return None
    else:
        x_num = (p1[0]*p2[1] - p1[1]*p2[0]) * (p3[0] - p4[0]) - (p1[0] - p2[0]) * (p3[0] * p4[1] - p3[1] * p4[0])
        y_num = (p1[0]*p2[1] - p1[1]*p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] * p4[1] - p3[1] * p4[0])
        return x_num / denominator, y_num / denominator


def is_upcoming(p1, v, p2):
    diff_x = p1[0] - p2[0]
    diff_y = p1[1] - p2[1]

    return ((diff_x < 0 < v[0]) or (diff_x > 0 > v[0])) and ((diff_y < 0 < v[1]) or (diff_y > 0 > v[1]))


def part1(data, min_p=200000000000000, max_p=400000000000000):
    stones = parse_data(data)

    collide = 0
    for s1, s2 in combinations(stones, 2):
        intersection_point = intersect_in_2d(s1, s2)
        if intersection_point is not None:
            if all([
                min_p <= intersection_point[0] <= max_p,
                min_p <= intersection_point[1] <= max_p,
                is_upcoming(s1[0], s1[1], intersection_point),
                is_upcoming(s2[0], s2[1], intersection_point),
            ]):
                collide += 1

    return collide


def part2(data):
    stones = parse_data(data)

    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    vx = Symbol('vx')
    vy = Symbol('vy')
    vz = Symbol('vz')

    equations = []
    time_symbols = []

    for i, stone in enumerate(stones[:3]):
        stone_time = Symbol('t' + str(i))
        eqx = x + vx * stone_time - stone[0][0] - stone[1][0] * stone_time
        eqy = y + vy * stone_time - stone[0][1] - stone[1][1] * stone_time
        eqz = z + vz * stone_time - stone[0][2] - stone[1][2] * stone_time

        equations += [eqx, eqy, eqz]
        time_symbols += [stone_time]

    result = solve_poly_system(equations, *([x, y, z, vx, vy, vz] + time_symbols))

    return sum(list(result[0])[0:3])


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 7, 27) == 2
    assert part2(test_1.splitlines()) == 47

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

