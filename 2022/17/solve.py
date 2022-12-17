#!/usr/bin/env python
from collections import defaultdict

test_1 = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""
test_2 = """"""


class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError( key )
        else:
            ret = self[key] = self.default_factory(key)
            return ret


def print_cave(max_y, cave):
    for y in range(max_y+3, -1, -1):
        print("".join([str(cave[(x, y)]) for x in range(0,9)]))


def let_it_fall(data, block_count=2022):
    cave = keydefaultdict(lambda c: 1 if c[0] in [0, 8] or c[1] == 0 else 0)
    jets = [j for j in data[0]]
    max_y = 0

    blocks = [
        lambda l, b: [(l, b), (l + 1, b), (l + 2, b), (l + 3, b)],
        lambda l, b: [(l + 1, b), (l, b + 1), (l + 1, b + 1), (l + 2, b + 1), (l + 1, b + 2)],
        lambda l, b: [(l, b), (l + 1, b), (l + 2, b), (l + 2, b + 1), (l + 2, b + 2)],
        lambda l, b: [(l, b), (l, b + 1), (l, b + 2), (l, b + 3)],
        lambda l, b: [(l, b), (l, b + 1), (l + 1, b), (l + 1, b + 1)],
    ]

    i = 0
    while i < block_count:
        cur_block = blocks.pop(0)
        cur_block_y = max_y + 4
        cur_block_x = 3

        cur_block_data = cur_block(cur_block_x, cur_block_y)

        while sum([cave[p] for p in cur_block_data]) == 0:
            jet = jets.pop(0)
            if jet == '>' and sum([cave[p] for p in cur_block(cur_block_x + 1, cur_block_y)]) == 0:
                cur_block_x += 1
            elif jet == '<' and sum([cave[p] for p in cur_block(cur_block_x - 1, cur_block_y)]) == 0:
                cur_block_x -= 1

            jets.append(jet)

            cur_block_y -= 1
            cur_block_data = cur_block(cur_block_x, cur_block_y)

        cur_block_data = cur_block(cur_block_x, cur_block_y + 1)
        for p in cur_block_data:
            cave[p] = 1
            max_y = max(max_y, p[1])
        blocks.append(cur_block)
        i += 1

    print(max_y)
    return max_y


def part1(data):
    return let_it_fall(data, 2022)


def part2(data):
    return let_it_fall(data, 1000000000000)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 3068
    assert part2(test_1.splitlines()) == 1514285714288

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))  # 3101 is too low, 3148 is too high
    print(part2(data.splitlines()))

