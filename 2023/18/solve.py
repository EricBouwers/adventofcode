#!/usr/bin/env python

test_1 = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
test_2 = """"""


def take_step(dir, pos):
    return pos[0] + dir[0], pos[1] + dir[1]


def parse_data(data):
    return [(l.split()[0], int(l.split()[1]), l.split()[2][1:-1]) for l in data]


def shoelace_surface(coords):
    shoe_surface = 0
    for p1, p2 in zip(coords, coords[1:] + [coords[0]]):
        shoe_surface += p1[0] * p2[1] - p2[0] * p1[1]

    return abs(shoe_surface / 2)


def part1(data):
    steps = parse_data(data)
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}

    edge = []
    perimeter = 0
    coor = (0, 0)
    for step in steps:
        dist, dir = step[1], directions[step[0]]
        perimeter += dist
        coor = take_step((dir[0] * dist, dir[1] * dist), coor)
        edge.append(coor)

    return shoelace_surface(edge) + perimeter/2 + 1


def part2(data):
    steps = parse_data(data)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    edge = []
    perimeter = 0
    coor = (0, 0)
    for step in steps:
        dist, dir = int(step[2][1:-1], 16), directions[int(step[2][-1])]
        perimeter += dist
        coor = take_step((dir[0] * dist, dir[1] * dist), coor)
        edge.append(coor)

    return shoelace_surface(edge) + perimeter/2 + 1


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 62
    assert part2(test_1.splitlines()) == 952408144115

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
