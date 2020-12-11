#!/usr/bin/env python
from collections import defaultdict

test_1 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def parse_seats(data):
    seats = {}
    for i, l in enumerate(data):
        for j, c in enumerate(l):
            seats[(i, j)] = c

    return seats


def update_seats(seats, neighbours, adj=3):
    new_seats = {}
    for coor, seat in seats.items():
        if seat == '.':
            new_seats[coor] = seat
        else:
            adjacent = [seats[new_coor] for new_coor in neighbours[coor]]
            if seat == 'L' and sum([x == '#' for x in adjacent]) == 0:
                new_seats[coor] = '#'
            elif seat == '#' and sum([x == '#' for x in adjacent]) > adj:
                new_seats[coor] = 'L'
            else:
                new_seats[coor] = seat

    return new_seats


def part1(data):
    seats = parse_seats(data)
    neighbours = {}

    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            neighbours[(i, j)] = [x for x in [
                (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                (i, j - 1), (i, j + 1),
                (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)] if x in seats]

    new_seats = update_seats(seats, neighbours)
    while sum([1 for s in seats if seats[s] != new_seats[s]]) > 0:
        seats = new_seats
        new_seats = update_seats(seats, neighbours)

    return sum([s == '#' for s in new_seats.values()])


def part2(data):
    seats = parse_seats(data)
    neighbours = defaultdict(list)
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                coor = (i+d[0], j+d[1])
                while coor in seats and seats[coor] == '.':
                    coor = (coor[0] + d[0], coor[1] + d[1])
                if coor in seats:
                    neighbours[(i, j)].append(coor)

    new_seats = update_seats(seats, neighbours, 4)
    while sum([1 for s in seats if seats[s] != new_seats[s]]) > 0:
        seats = new_seats
        new_seats = update_seats(seats, neighbours, 4)

    return sum([s == '#' for s in new_seats.values()])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 37
    assert part2(test_1.splitlines()) == 26

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

