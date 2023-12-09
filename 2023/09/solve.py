#!/usr/bin/env python

test_1 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
test_2 = """"""


def parse_data(data):
    lines = [[int(x) for x in line.split(" ")] for line in data]
    return lines


def next_num(sequence):
    if len(set(sequence)) == 1:
        return sequence[0], sequence[0]
    else:
        new_seq = [j-i for i, j in zip(sequence[:-1], sequence[1:])]
        inc = next_num(new_seq)
        return sequence[0] - inc[0], sequence[-1] + inc[1]


def part1(data):
    parsed = parse_data(data)
    return sum([next_num(x)[1] for x in parsed])


def part2(data):
    parsed = parse_data(data)
    return sum([next_num(x)[0] for x in parsed])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 114
    assert part2(test_1.splitlines()) == 2

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

