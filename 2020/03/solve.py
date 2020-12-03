#!/usr/bin/env python

test_1 = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data, right=3, down=1):
    current_row = 0
    steps = 0
    max_row = len(data) - 1
    columns = len(data[0])

    trees = 0
    while current_row < max_row:
        current_row += down
        steps = steps + 1
        current_column = (steps * right) % columns
        trees += 1 if data[current_row][current_column] == "#" else 0

    return trees


def part2(data):
    result = 1
    for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees = part1(data, r, d)
        result = result * trees
    return result


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 7
    assert part1(test_1.splitlines(), 1, 2) == 2
    assert part2(test_1.splitlines()) == 336

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

