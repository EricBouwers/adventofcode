#!/usr/bin/env python
from collections import defaultdict, deque

test_1 = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
test_2 = """"""


def parse_data(data):
    return [ -int(d[1:]) if d[0] == 'L' else int(d[1:]) for d in data]


def part1(data):
    ins = parse_data(data)
    counts = defaultdict(lambda: 0)

    queue = deque([x for x in range(0,100)])
    queue.rotate(50)
    for i in ins:
        queue.rotate(i)
        counts[queue[0]] += 1
    return counts[0]


def part2(data):
    ins = parse_data(data)
    counts = defaultdict(lambda: 0)

    queue = deque([x for x in range(0,100)])
    queue.rotate(50)
    for i in ins:
        step = 1 if i > 0 else -1
        for x in range(0,i,step):
            queue.rotate(step)
            counts[queue[0]] += 1
    return counts[0]


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 3
    assert part2(test_1.splitlines()) == 6

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

# 664 too low