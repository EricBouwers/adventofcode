#!/usr/bin/env python

test_1 = """16,1,2,0,4,2,7,1,2,14"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data):
    positions = [int(d) for d in data[0].split(',')]
    lowest_cost = sum(positions)
    for p in {p:p for p in positions}.keys():
        p_cost = sum([abs(x - p) for x in positions])
        lowest_cost = p_cost if p_cost < lowest_cost else lowest_cost
    return lowest_cost


def part2(data):
    positions = [int(d) for d in data[0].split(',')]
    lowest_cost = sum(positions)**500
    for p in range(min(positions), max(positions) + 1):
        p_cost = sum([((abs(x - p))*(abs(x - p)+1) / 2) for x in positions])
        lowest_cost = p_cost if p_cost < lowest_cost else lowest_cost
    return lowest_cost


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 37
    assert part2(test_1.splitlines()) == 168

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

