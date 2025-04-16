#!/usr/bin/env python

test_1 = """2x3x4
1x1x10"""


def parse_data(data):
    return map(lambda p: [int(x) for x in p.split("x")], data)


def part1(data):
    presents = parse_data(data)

    total = 0
    for p in presents:
        [l, w, h] = p
        sides = [l*w, w*h, h*l]
        total += 2*sum(sides) + min(sides)

    return total


def part2(data):
    presents = parse_data(data)

    total = 0
    for p in presents:
        [l, w, h] = p
        sides = [l+w, l+h, h+w]
        total += 2*min(sides) + l*w*h

    return total


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 101
    assert part2(test_1.splitlines()) == 48

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

