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

    blocks = [
        lambda l, b: [(l, b), (l + 1, b), (l + 2, b), (l + 3, b)],
        lambda l, b: [(l + 1, b), (l, b + 1), (l + 1, b + 1), (l + 2, b + 1), (l + 1, b + 2)],
        lambda l, b: [(l, b), (l + 1, b), (l + 2, b), (l + 2, b + 1), (l + 2, b + 2)],
        lambda l, b: [(l, b), (l, b + 1), (l, b + 2), (l, b + 3)],
        lambda l, b: [(l, b), (l, b + 1), (l + 1, b), (l + 1, b + 1)],
    ]

    cache = {}

    i = 0
    max_y, jeti, blocki = 0, 0, 0
    jetlen, blocklen = len(jets), len(blocks)
    last_line = "".join([str(cave[(x, y)]) for x in range(1, 8) for y in range(max_y, max_y - 10, -1)])
    add_y = 0
    cache_used = False

    while i < block_count:
        cache_key = (last_line, jeti, blocki)
        if cache_key in cache and not cache_used:
            prev_i, prev_y = cache[cache_key]
            cycle_len = i - prev_i
            steps = int((block_count - i) / cycle_len)
            i = i + (steps * cycle_len)
            add_y = (max_y - prev_y) * steps
            cache_used = True
        else:
            cache[cache_key] = i, max_y

            cur_block = blocks[blocki]
            cur_block_y = max_y + 4
            cur_block_x = 3

            cur_block_data = cur_block(cur_block_x, cur_block_y)

            while sum([cave[p] for p in cur_block_data]) == 0:
                jet = jets[jeti]
                if jet == '>' and sum([cave[p] for p in cur_block(cur_block_x + 1, cur_block_y)]) == 0:
                    cur_block_x += 1
                elif jet == '<' and sum([cave[p] for p in cur_block(cur_block_x - 1, cur_block_y)]) == 0:
                    cur_block_x -= 1

                jeti = (jeti + 1) % jetlen

                cur_block_y -= 1
                cur_block_data = cur_block(cur_block_x, cur_block_y)

            cur_block_data = cur_block(cur_block_x, cur_block_y + 1)
            for p in cur_block_data:
                cave[p] = 1
                max_y = max(max_y, p[1])

            i += 1
            blocki = (blocki + 1) % blocklen
            last_line = "".join([str(cave[(x,y)]) for x in range(1,8) for y in range(max_y, max_y-10, -1)])

    print(max_y + add_y)
    return max_y + add_y


def part1(data):
    return let_it_fall(data, 2022)


def part2(data):
    return let_it_fall(data, 1000000000000)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 3068
    assert part2(test_1.splitlines()) == 1514285714288

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
