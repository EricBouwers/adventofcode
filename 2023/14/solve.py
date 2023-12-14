#!/usr/bin/env python

test_1 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
test_2 = """"""


def parse_data(data):
    return [[c for c in line] for line in data], len(data), len(data[0])


def print_grid(g):
    for line in g:
        print(''.join(line))


def roll_north(grid, max_x, max_y):
    for x in range(0, max_x):
        last_valid_pos = None
        for y in range(0, max_y):
            cur_char = grid[y][x]
            if cur_char == '.' and last_valid_pos is None:
                last_valid_pos = (x, y)
            elif cur_char == '#':
                last_valid_pos = None
            elif cur_char == 'O' and last_valid_pos is not None:
                grid[y][x] = '.'
                grid[last_valid_pos[1]][last_valid_pos[0]] = 'O'
                last_valid_pos = (last_valid_pos[0], last_valid_pos[1]+1)


def roll_south(grid, max_x, max_y):
    for x in range(0, max_x):
        last_valid_pos = None
        for y in range(max_y-1, -1, -1):
            cur_char = grid[y][x]
            if cur_char == '.' and last_valid_pos is None:
                last_valid_pos = (x, y)
            elif cur_char == '#':
                last_valid_pos = None
            elif cur_char == 'O' and last_valid_pos is not None:
                grid[y][x] = '.'
                grid[last_valid_pos[1]][last_valid_pos[0]] = 'O'
                last_valid_pos = (last_valid_pos[0], last_valid_pos[1]-1)


def roll_west(grid, max_x, max_y):
    for y in range(0, max_y):
        last_valid_pos = None
        for x in range(0, max_x):
            cur_char = grid[y][x]
            if cur_char == '.' and last_valid_pos is None:
                last_valid_pos = (x, y)
            elif cur_char == '#':
                last_valid_pos = None
            elif cur_char == 'O' and last_valid_pos is not None:
                grid[y][x] = '.'
                grid[last_valid_pos[1]][last_valid_pos[0]] = 'O'
                last_valid_pos = (last_valid_pos[0]+1, last_valid_pos[1])


def roll_east(grid, max_x, max_y):
    for y in range(0, max_y):
        last_valid_pos = None
        for x in range(max_x-1, -1, -1):
            cur_char = grid[y][x]
            if cur_char == '.' and last_valid_pos is None:
                last_valid_pos = (x, y)
            elif cur_char == '#':
                last_valid_pos = None
            elif cur_char == 'O' and last_valid_pos is not None:
                grid[y][x] = '.'
                grid[last_valid_pos[1]][last_valid_pos[0]] = 'O'
                last_valid_pos = (last_valid_pos[0]-1, last_valid_pos[1])


def count_support(grid, max_y):
    total = 0
    for i, y in enumerate(grid):
        total += sum([c == 'O' for c in y]) * (max_y - i)
    return total


def part1(data):
    grid, max_y, max_x = parse_data(data)
    roll_north(grid, max_x, max_y)
    return count_support(grid, max_y)


def part2(data):
    grid, max_y, max_x = parse_data(data)

    cache = {}
    i = 0
    while i < 1000000000:
        roll_north(grid, max_x, max_y)
        roll_west(grid, max_x, max_y)
        roll_south(grid, max_x, max_y)
        roll_east(grid, max_x, max_y)

        pg = ''.join([''.join(line) for line in grid])
        if pg in cache:
            round_size = i - cache[pg][0]
            if i + round_size < 1000000000:
                to_go = 1000000000 - i
                i += int(to_go / round_size) * round_size
                cache = {}
        else:
            cache[pg] = (i, count_support(grid, max_y))

        i += 1

    return count_support(grid, max_y)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 136
    assert part2(test_1.splitlines()) == 64

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))