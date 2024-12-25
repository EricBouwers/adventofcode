#!/usr/bin/env python

test_1 = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""
test_2 = """"""


def parse_data(data):
    items = []
    cur_item = {}
    cur_y = 0
    for d in data:
        if not d:
            items.append(cur_item)
            cur_item = {}
            cur_y = 0
        else:
            for x, c in enumerate(d):
                if c == '#':
                    cur_item[complex(x, cur_y)] = '#'
            cur_y += 1

    items.append(cur_item)
    return items


def part1(data):
    items = parse_data(data)

    locks = [i for i in items if 0 in i]
    keys = [i for i in items if 0 not in i]

    overlaps = 0
    for l in locks:
        for k in keys:
            overlaps += 1 if l.keys().isdisjoint(k.keys()) else 0

    return overlaps


def part2(data):
    parsed = parse_data(data)
    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 3
    assert part2(test_1.splitlines()) == None

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

