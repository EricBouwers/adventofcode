#!/usr/bin/env python

test_1 = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
test_2 = """"""


def parse_data(data):
    robots = []
    for l in data:
        p, v = l.split(" ")
        p = tuple([int(x) for x in p[2:].split(',')])
        v = tuple([int(x) for x in v[2:].split(',')])
        robots.append((p, v))

    return robots


def take_step(r, max_x, max_y):
    new_x = (r[0][0] + r[1][0]) % max_x
    new_y = (r[0][1] + r[1][1]) % max_y
    return (new_x, new_y), r[1]


def count_kwadrants(robots, max_x, max_y):
    x_len = max_x // 2
    y_len = max_y // 2

    kwadrant_1 = len([r for r in robots if 0 <= r[0][0] < x_len and 0 <= r[0][1] < y_len])
    kwadrant_2 = len([r for r in robots if x_len < r[0][0] < max_x and 0 <= r[0][1] < y_len])
    kwadrant_3 = len([r for r in robots if 0 <= r[0][0] < x_len and y_len < r[0][1] < max_y])
    kwadrant_4 = len([r for r in robots if x_len < r[0][0] < max_x and y_len < r[0][1] < max_y])

    return kwadrant_1 * kwadrant_2 * kwadrant_3 * kwadrant_4


def part1(data, max_x=101, max_y=103):
    robots = parse_data(data)

    for i in range(0, 100):
        robots = [take_step(r, max_x, max_y) for r in robots]

    return count_kwadrants(robots, max_x, max_y)


def print_robots(robots, x, y):
    for i in range(y):
        line = ""
        for j in range(x):
            line += "*" if (i, j) in robots else ' '

        print(line)


def part2(data, max_x=101, max_y=103):
    robots = parse_data(data)

    for i in range(0, 100000):
        robots = [take_step(r, max_x, max_y) for r in robots]
        print_robots(set([r[0] for r in robots]), max_x, max_y)


if __name__ == '__main__':

    assert part1(test_1.splitlines(), max_x=11, max_y=7) == 12

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

