#!/usr/bin/env python
from collections import defaultdict

test_1 = """125 17"""
test_2 = """"""


def parse_data(data):
    return [int(x) for x in data.split()]


def get_stones(stone):
    if stone == 0:
        return [1]
    else:
        stone_char = str(stone)
        if len(stone_char) % 2 == 0:
            half = len(stone_char) // 2
            return [int(stone_char[0:half]), int(stone_char[half:])]
        else:
            return [stone * 2024]


def blink(stones):
    new_stones = []
    for s in stones:
        new_stones.extend(get_stones(s))
    return new_stones


def dict_blink(stones):
    new_stones = defaultdict(lambda: 0)
    for s in stones.keys():
        for new_s in get_stones(s):
            new_stones[new_s] += stones[s]
    
    return new_stones
    

def part1(data):
    stones = parse_data(data)

    for i in range(0, 25):
        stones = blink(stones)

    return len(stones)


def part2(data):
    stones = defaultdict(lambda: 0)
    for s in parse_data(data):
        stones[s] += 1

    for i in range(0, 75):
        stones = dict_blink(stones)

    return sum(stones.values())


if __name__ == '__main__':

    assert part1(test_1.splitlines()[0]) == 55312

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()[0]))
    print(part2(data.splitlines()[0]))

