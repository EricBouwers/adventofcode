#!/usr/bin/env python
from collections import defaultdict

test_1 = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
test_2 = """"""


def parse_data(data):
    cave = defaultdict(lambda: 0)

    for d in data:
        prev_c = None
        for c in d.split(" -> "):
            coor = (int(c.split(',')[0]), int(c.split(',')[1]))
            if prev_c is not None:
                if coor[0] == prev_c[0]:
                    step = (0, 1) if prev_c[1] < coor[1] else (0, -1)
                else:
                    step = (1, 0) if prev_c[0] < coor[0] else (-1, 0)

                cur_cor = prev_c
                cave[cur_cor] = 1
                while cur_cor != coor:
                    cur_cor = (cur_cor[0] + step[0], cur_cor[1] + step[1])
                    cave[cur_cor] = 1

            prev_c = coor

    return cave


def take_step(sand_cor, cave):
    for new_cor in [
        (sand_cor[0], sand_cor[1]+1),
        (sand_cor[0]-1, sand_cor[1]+1),
        (sand_cor[0]+1, sand_cor[1]+1)]:
        if cave[new_cor] == 0:
            return new_cor
    return sand_cor


def part1(data):
    cave = parse_data(data)

    max_y = max([y for x,y in cave.keys()])

    sand_cor = (500, 0)
    while sand_cor[1] < max_y:
        new_cor = take_step(sand_cor, cave)
        if new_cor == sand_cor:
            cave[new_cor] = 2
            sand_cor = (500, 0)
        else:
            sand_cor = new_cor

    return sum([v == 2 for v in cave.values()])


class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError( key )
        else:
            ret = self[key] = self.default_factory(key)
            return ret


def part2(data):
    old_cave = parse_data(data)
    max_y = max([y for x, y in old_cave.keys()])
    cave = keydefaultdict(lambda x: 1 if (x[1] > max_y + 1) else 0)
    cave.update(old_cave)

    sand_cor = (500, 0)
    all_full = False
    while not all_full:
        new_cor = take_step(sand_cor, cave)
        if new_cor == (500, 0):
            all_full = True
        if new_cor == sand_cor:
            cave[new_cor] = 2
            sand_cor = (500, 0)
        else:
            sand_cor = new_cor

    return sum([v == 2 for v in cave.values()])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 24
    assert part2(test_1.splitlines()) == 93

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

