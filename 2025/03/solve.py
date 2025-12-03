#!/usr/bin/env python

test_1 = """987654321111111
811111111111119
234234234234278
818181911112111
"""
test_2 = """"""


def parse_data(data):
    return [(d, list(map(int, d))) for d in data]


def calculate_jolts(bs, bi, numbers_left):
    if numbers_left < 0:
        return 0

    if numbers_left == 0:
        my_jolt = max(bi)
    else:
        my_jolt = max(bi[0:-numbers_left])

    my_jolt_i = bs.index(str(my_jolt))
    return (my_jolt * 10**numbers_left) + calculate_jolts(bs[my_jolt_i+1:],bi[my_jolt_i+1:],numbers_left-1)

def part1(data):
    banks = parse_data(data)

    total_jolts = 0
    for bs, bi in banks:
        total_jolts += calculate_jolts(bs, bi, 1)

    return total_jolts


def part2(data):
    banks = parse_data(data)

    total_jolts = 0
    for bs, bi in banks:
        total_jolts += calculate_jolts(bs, bi, 11)

    return total_jolts


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 357
    assert part2(test_1.splitlines()) == 3121910778619

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

