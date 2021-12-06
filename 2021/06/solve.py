#!/usr/bin/env python
from collections import defaultdict

test_1 = """3,4,3,1,2"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data, days=80):
    fish = [int(d) for d in data[0].split(',')]
    for d in range(0, days):
        new_fish = []
        spawn_fish = 0
        for f in fish:
            new_fish.append(6 if f == 0 else f - 1)
            spawn_fish += 1 if f == 0 else 0
        fish = new_fish + [8 for _ in range(0, spawn_fish)]
    return len(fish)


def part2(data, days=256):
    fish = defaultdict(lambda: 0)
    for d in data[0].split(','):
        fish[int(d)] += 1

    to_add = defaultdict(lambda: 0)
    for d in range(0, days):
        fish[d % 7] += to_add[d]
        to_add[d] = 0
        to_spawn = fish[d % 7]
        new_spawn_day = d + 9
        to_add[new_spawn_day] = to_spawn

    return sum(fish.values()) + sum(to_add.values())


if __name__ == '__main__':

    assert part1(test_1.splitlines(), days=12) == 17
    assert part1(test_1.splitlines()) == 5934
    assert part2(test_1.splitlines(), days=12) == 17
    assert part2(test_1.splitlines(), days=80) == 5934
    assert part2(test_1.splitlines(), days=256) == 26984457539
    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
