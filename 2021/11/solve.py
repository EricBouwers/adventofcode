#!/usr/bin/env python

test_1 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def parse_map(m):
    octo_map = {}
    for y, l in enumerate(m):
        for x, v in enumerate(l):
            octo_map[(y, x)] = int(v)

    return octo_map


def neighbours(c):
    return [
        (c[0], c[1] - 1),
        (c[0], c[1] + 1),
        (c[0] - 1, c[1]),
        (c[0] + 1, c[1]),
        (c[0] - 1, c[1] - 1),
        (c[0] + 1, c[1] + 1),
        (c[0] - 1, c[1] + 1),
        (c[0] + 1, c[1] - 1),
    ]


def print_map(m):
    for y in range(0, 10):
        line = ''
        for x in range(0, 10):
            line += str(m[(y, x)]) + " "
        print(line)


def part1(data, steps=100):
    levels = parse_map(data)
    flashes = 0
    for step in range(0, steps):
        processed, levels = take_step(levels)
        flashes += len(processed)

    return flashes


def take_step(levels):
    levels = {k: v + 1 for k, v in levels.items()}
    to_flash = set([c for c, l in levels.items() if l > 9])
    processed = set()
    while len(to_flash) > 0:
        f = to_flash.pop()
        if f not in processed:
            processed.add(f)
            for n in neighbours(f):
                if n in levels:
                    levels[n] += 1
                    if levels[n] > 9 and n not in processed:
                        to_flash.add(n)
    for p in processed:
        levels[p] = 0
    return processed, levels


def part2(data):
    levels = parse_map(data)
    processed = []
    steps = 0
    while len(processed) != 100:
        processed, levels = take_step(levels)
        steps += 1

    return steps


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 1656
    assert part2(test_1.splitlines()) == 195

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

