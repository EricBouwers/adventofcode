#!/usr/bin/env python
from collections import defaultdict

test_1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
test_2 = """"""


def parse_data(data):
    schema = defaultdict(lambda: '.')
    numbers = {}
    symbols = {}

    cur_number, begin_pos, end_pos = '', None, None
    for y, line in enumerate(data):
        if cur_number is not '':
            numbers[(begin_pos, end_pos)] = int(cur_number)
            cur_number, begin_pos, end_pos = '', None, None

        for x, c in enumerate(line):
            if c.isdigit():
                cur_number = cur_number + c
                begin_pos = (x, y) if begin_pos is None else begin_pos
                end_pos = (x, y)
            else:
                if c is not '.':
                    symbols[(x, y)] = c
                if cur_number is not '':
                    numbers[(begin_pos, end_pos)] = int(cur_number)
                    cur_number, begin_pos, end_pos = '', None, None
            schema[(x, y)] = c

    if cur_number is not '':
        numbers[(begin_pos, end_pos)] = int(cur_number)

    return numbers, symbols, schema


def add_pos(p1, p2):
    return p1[0]+p2[0], p1[1]+p2[1]


def boxes_overlap(left_upper1, right_bottom1, left_upper2, right_bottom2):
    # If one rectangle is left of the other
    if left_upper1[0] > right_bottom2[0] or left_upper2[0] > right_bottom1[0]:
        return False

    # If one rectangle is above other
    if right_bottom1[1] < left_upper2[1] or right_bottom2[1] < left_upper1[1]:
        return False

    return True


def part1(data):
    numbers, symbols, schema = parse_data(data)

    parts_sum = 0
    for position, number in numbers.items():
        wider_box = (add_pos(position[0], (-1, -1)), add_pos(position[1], (1, 1)))
        if any([boxes_overlap(wider_box[0], wider_box[1], c, c) for c in symbols.keys()]):
            parts_sum += number

    return parts_sum


def part2(data):
    numbers, symbols, schema = parse_data(data)

    gear_ratio = 0
    for position, symbol in [(pos, sym) for (pos, sym) in symbols.items() if sym is '*']:
        wider_box = (add_pos(position, (-1, -1)), add_pos(position, (1, 1)))
        attached_numbers = [
            number for position, number in numbers.items() if boxes_overlap(
                position[0], position[1], wider_box[0], wider_box[1]
            )
        ]
        if len(attached_numbers) == 2:
            gear_ratio += attached_numbers[0] * attached_numbers[1]

    return gear_ratio


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 4361
    assert part2(test_1.splitlines()) == 467835

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
