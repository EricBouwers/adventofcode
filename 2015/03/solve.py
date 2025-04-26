#!/usr/bin/env python
from collections import defaultdict

test_1 = """>"""
test_2 = """^>v<"""
test_3 = """^v^v^v^v^v"""


steps = {
    '>': [1, 0],
    '<': [-1, 0],
    '^': [0, -1],
    'v': [0, 1]
}


def parse_data(data):
    return data[0]


def take_step(pos, step):
    return (pos[0] + steps[step][0], pos[1] + steps[step][1])


def part1(data):
    instructions = parse_data(data)
    pos = (0,0)
    visited = {pos}

    for p in instructions:
        pos = take_step(pos, p)
        visited.add(pos)

    return len(visited)


def part2(data):
    instructions = parse_data(data)
    santa_pos = (0,0)
    robo_santa_pos = (0, 0)
    visited = {santa_pos, robo_santa_pos}

    for i, p in enumerate(instructions):
        if i % 2 == 0:
            santa_pos = take_step(santa_pos, p)
            visited.add(santa_pos)
        else:
            robo_santa_pos = take_step(robo_santa_pos, p)
            visited.add(robo_santa_pos)

    return len(visited)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 2
    assert part1(test_2.splitlines()) == 4
    assert part2(test_3.splitlines()) == 11

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

