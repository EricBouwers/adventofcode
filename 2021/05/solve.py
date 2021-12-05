#!/usr/bin/env python
from collections import defaultdict

test_1 = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_data(data):
    lines = []
    for line in data:
        parts = line.split(' -> ')
        start = [int(x) for x in parts[0].split(',')]
        end = [int(x) for x in parts[1].split(',')]
        lines.append((start, end))
    return lines


def print_board(b):
    print(b)
    for y in range(0,10):
        line = ''
        for x in range(0, 10):
            line += str(b[(x, y)]) + " "
        print(line)


def draw_lines(lines):
    board = defaultdict(lambda: 0)
    for l in lines:
        x_step = 0 if l[0][0] == l[1][0] else 1 if l[0][0] < l[1][0] else -1
        y_step = 0 if l[0][1] == l[1][1] else 1 if l[0][1] < l[1][1] else -1
        x, y = l[0]
        while not (x == l[1][0] and y == l[1][1]):
            board[(x, y)] += 1
            x += x_step
            y += y_step
        board[(x, y)] += 1
    return board


def part1(data):
    lines = parse_data(data)
    lines = [l for l in lines if l[0][0] == l[1][0] or l[0][1] == l[1][1]]
    board = draw_lines(lines)
    return len([x for x in board.values() if x > 1])


def part2(data):
    lines = parse_data(data)
    board = draw_lines(lines)
    return len([x for x in board.values() if x > 1])


if __name__ == '__main__':
    assert part1(test_1.splitlines()) == 5
    assert part2(test_1.splitlines()) == 12

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
