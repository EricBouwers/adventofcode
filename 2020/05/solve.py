#!/usr/bin/env python
from math import floor, ceil

test_1 = """FBFBBFFRLR"""
test_2 = """BFFFBBFRRR"""
test_3 = """FFFBBBFRRR"""
test_4 = """BBFFBBFRLL"""


def seat_id(bp):
    row = [0, 127]
    column = [0, 7]
    for c in bp[0:7]:
        half = ceil((row[1] - row[0]) / 2)
        if c == 'F':
            row = [row[0], row[1] - half]
        else:
            row = [row[0] + half, row[1]]

    for c in bp[7:]:
        half = ceil((column[1] - column[0]) / 2)
        if c == 'L':
            column = [column[0], column[1] - half]
        else:
            column = [column[0] + half, column[1]]

    return (row[0] * 8) + column[0]


def part1(data):
    return max([seat_id(bp) for bp in data.splitlines()])


def part2(data):
    given_seats = [seat_id(bp) for bp in data.splitlines()]

    # fast way by printing and finding the odd number in the list
    # all_seats = {((row * 8) + col) for col in range(0, 7) for row in range(0, 127)}
    # print(all_seats - set(given_seats))

    # generic way by calculating
    given_seats = sorted(given_seats)
    cur_seat = given_seats[0]
    for next_seat in given_seats[1:]:
        if cur_seat+1 == next_seat:
            cur_seat = next_seat
        else:
            return cur_seat+1


if __name__ == '__main__':

    assert seat_id(test_1) == 357
    assert seat_id(test_2) == 567
    assert seat_id(test_3) == 119
    assert seat_id(test_4) == 820

    with open('input') as f:
        data = f.read()

    print(part1(data))
    print(part2(data))

