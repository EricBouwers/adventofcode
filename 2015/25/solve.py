#!/usr/bin/env python

test_1 = """1
6
"""
test_2 = """6
6
"""


def parse_data(data):
    return [int(data[0]), int(data[1])]

def part1(data):
    row, col = parse_data(data)

    cur_row, cur_col = 1, 1
    max_row, max_col = 1, 1
    code = 20151125

    while True:
        if cur_col == col and cur_row == row:
            return code
        else:
            code = (code * 252533) % 33554393
            if cur_row == 1:
                max_row += 1
                cur_row = max_row
                cur_col = 1
            else:
                cur_row -= 1
                cur_col += 1

def part2(data):
    parsed = parse_data(data)
    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 33511524
    assert part1(test_2.splitlines()) == 27995004

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

