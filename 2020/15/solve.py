#!/usr/bin/env python
from collections import defaultdict

test_1 = """0,3,6"""
test_2 = """1,3,2"""
test_3 = """3,1,2"""


def part1(data, end=2020):
    last_seen = defaultdict(list)
    last_spoken = 0
    for i, n in enumerate(data[0].split(',')):
        last_spoken = int(n)
        last_seen[last_spoken].append(i+1)
    idx = len(last_seen) + 1

    while idx < end+1:
        last_seens = last_seen[last_spoken]
        if len(last_seens) == 1:
            last_spoken = 0
        else:
            last_spoken = last_seens[-1] - last_seens[-2]

        last_seen[last_spoken].append(idx)
        if len(last_seen[last_spoken]) > 2:
            last_seen[last_spoken] = last_seen[last_spoken][-2:]

        idx += 1

    return last_spoken


def part2(data):
    return part1(data, 30000000)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 436
    assert part1(test_2.splitlines()) == 1
    assert part1(test_3.splitlines()) == 1836
    assert part2(test_1.splitlines()) == 175594
    assert part2(test_2.splitlines()) == 2578
    assert part2(test_3.splitlines()) == 362

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

