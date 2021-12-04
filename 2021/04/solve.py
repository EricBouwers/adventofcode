#!/usr/bin/env python

import re

test_1 = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
test_2 = """"""
test_3 = """"""
test_4 = """"""

def parse_boards(data):
    boards = []
    board = {}
    y = 0
    for d in data:
        if not d:
            boards.append(board)
            board = {}
            y = 0
        else:
            x_pos = 0
            for n in re.split("\s+", d):
                if n:
                    board[(x_pos,y)] = int(n)
                    x_pos += 1
            y += 1
    boards.append(board)
    return boards 

def print_board(b):
    for y in range(0,5):
        line = ''
        for x in range(0,5):
            line += str(b[(x,y)]) + " "
        print(line)

def has_won(b, nums):
    for y in range(0,5):
        row_full = True
        for x in range(0,5):
            row_full = row_full and b[(x,y)] in nums
        if row_full:
            return True

    for x in range(0,5):
        col_full = True
        for y in range(0,5):
            col_full = col_full and b[(x,y)] in nums
        if col_full:
            return True

    return False

def part1(data):
    numbers = [int(d) for d in data[0].split(',')]
    boards = parse_boards(data[2:])

    drawn_numbers = []
    for n in numbers:
        drawn_numbers.append(n)
        for b in boards:
            if has_won(b, drawn_numbers):
                return n * sum([x for x in b.values() if x not in drawn_numbers])
    
    return None


def part2(data):
    numbers = [int(d) for d in data[0].split(',')]
    boards = parse_boards(data[2:])

    drawn_numbers = []
    for n in numbers:
        drawn_numbers.append(n)
        if len(boards) == 1:
            if has_won(boards[0], drawn_numbers):
                return n * sum([x for x in boards[0].values() if x not in drawn_numbers])
        else:
            new_boards = []
            for b in boards:
                if not has_won(b, drawn_numbers):
                    new_boards.append(b)
            boards = new_boards

    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 4512
    assert part2(test_1.splitlines()) == 1924

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

