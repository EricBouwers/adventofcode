#!/usr/bin/env python
from collections import defaultdict

test_1 = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_data(data):
    algo = ""
    image = defaultdict(lambda: "0")

    line = data.pop(0)
    while line:
        algo = algo + line
        line = data.pop(0)

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            image[(x, y)] = "0" if c == "." else "1"

    return algo, image


def print_image(image):
    y_s = [c[1] for c in image.keys()]
    x_s = [c[0] for c in image.keys()]

    for y in range(min(y_s), max(y_s) + 1):
        print("".join([image[(x, y)] for x in range(min(x_s), max(x_s) + 1)]))


def enhance(image, algo, default):
    new_image = defaultdict(lambda: default)

    y_s = [c[1] for c in image.keys()]
    x_s = [c[0] for c in image.keys()]
    for y in range(min(y_s) - 1, max(y_s) + 2):
        for x in range(min(x_s) - 1, max(x_s) + 2):
            p = (x, y)
            new_image[p] = "0" if algo[
                int("".join([
                    image[(p[0] - 1, p[1] - 1)], image[(p[0], p[1] - 1)], image[(p[0] + 1, p[1] - 1)],
                    image[(p[0] - 1, p[1])], image[(p[0], p[1])], image[(p[0] + 1, p[1])],
                    image[(p[0] - 1, p[1] + 1)], image[(p[0], p[1] + 1)], image[(p[0] + 1, p[1] + 1)],
                ]), 2)
            ] == "." else "1"

    return new_image


def part1(data, steps=2):
    algo, image = parse_data(data)
    default = "0" if algo[0] == "." else "1"
    for i in range(0, steps):
        image = enhance(image, algo, default)
        # print_image(image)
        default = "0" if algo[int(default*9, 2)] == '.' else "1"

    return sum([v == "1" for v in image.values()])


def part2(data):
    return part1(data, steps=50)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 35
    assert part2(test_1.splitlines()) == 3351

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

