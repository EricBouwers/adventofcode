#!/usr/bin/env python
from collections import defaultdict

test_1 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
test_2 = """"""


def parse_data(data):
    grid = defaultdict(lambda: '.')
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c

    return grid, len(data[0]), len(data)


def take_steps(dir, pos, steps):
    return pos[0] + (steps * dir[0]), pos[1] + (steps * dir[1])


def has_xmas(dir, coor, grid):
    word = [grid[take_steps(dir, coor, n)] for n in range(0, 4)]
    return word == ['X', 'M', 'A', 'S']


def count_xmas(coor, grid):
    return sum([has_xmas(direction, coor, grid) for direction in [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]])


def get_a_coor(dir, coor, grid):
    my_word = [grid[take_steps(dir, coor, n)] for n in range(0, 3)]

    flipped_dir = (-dir[0], dir[1])
    middle_point = take_steps(dir, coor, 1)
    other_word = [
        grid[take_steps(flipped_dir, middle_point, -1)],
        grid[take_steps(flipped_dir, middle_point, 1)],
    ]

    if my_word == ['M', 'A', 'S'] and 'M' in other_word and 'S' in other_word:
        print(my_word, other_word)

    return middle_point if my_word == ['M', 'A', 'S'] and 'M' in other_word and 'S' in other_word else None


def get_a_coordinates_if_x_mas(coor, grid):
    return set([get_a_coor(direction, coor, grid) for direction in [
        (-1, -1), (1, -1),
        (-1, 1), (1, 1)
    ]])


def part1(data):
    grid, max_x, max_y = parse_data(data)
    x_coords = [k for k in grid.keys() if grid[k] == 'X']
    return sum([count_xmas(c, grid) for c in x_coords])


def part2(data):
    grid, max_x, max_y = parse_data(data)
    m_coords = [k for k in grid.keys() if grid[k] == 'M']
    a_coordinates = set()
    for c in m_coords:
        a_coordinates = a_coordinates.union(get_a_coordinates_if_x_mas(c, grid))
    return len(a_coordinates) - 1


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 18
    assert part2(test_1.splitlines()) == 9

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

