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


blocks = [
 lambda l, b: ([(l, b), (l+1, b), (l+2, b), (l+3, b)], l, l+3),
 lambda l, b: ([(l+1, b), (l, b+1), (l+1, b+1), (l+2, b+1), (l+1, b+2)], l, l+2),
 lambda l, b: ([(l, b), (l+1, b), (l+2, b), (l+2, b+1), (l+2, b+2)], l, l+2),
 lambda l, b: ([(l, b), (l, b+1), (l, b+2), (l, b+3)], l, l),
 lambda l, b: ([(l, b), (l, b+1), (l+1, b), (l+1, b+1)], l, l+1),
]


def print_cave(max_y, cave):
    for y in range(max_y+3, -1, -1):
        print("".join([str(cave[(x, y)]) for x in range(0,9)]))


def part1(data):
    cave = keydefaultdict(lambda c: 1 if c[0] in [0, 8] or c[1] == 0 else 0)
    jets = [j for j in data[0]]
    max_y = 0

    for i in range(0, 2022):
        cur_block = blocks.pop(0)
        cur_block_y = max_y + 4
        cur_block_x = 3

        cur_block_data = cur_block(cur_block_x, cur_block_y)

        while sum([cave[p] for p in cur_block_data[0]]) == 0:
            jet = jets.pop(0)
            if jet == '>' and cave[(cur_block_data[2]+1, cur_block_y)] == 0:
                cur_block_x += 1
                cur_block(cur_block_x, cur_block_y)
            elif jet == '<' and cave[(cur_block_data[1]-1, cur_block_y)] == 0:
                cur_block_x -= 1
                cur_block(cur_block_x, cur_block_y)

            jets.append(jet)

            cur_block_y -= 1
            cur_block_data = cur_block(cur_block_x, cur_block_y)

        cur_block_data = cur_block(cur_block_x, cur_block_y+1)
        for p in cur_block_data[0]:
            cave[p] = 1
            max_y = max(max_y, p[1])
        blocks.append(cur_block)

    print(max_y)
    return max_y


def part2(data):
    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 3068
    assert part2(test_1.splitlines()) == None

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))  # 3101 is too low
    print(part2(data.splitlines()))

