#!/usr/bin/env python
from functools import reduce
from math import sqrt
from operator import mul
import numpy as np
from numpy import rot90, flip, array2string

test_1 = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...

"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


class Tile(object):

    def __init__(self, rows):
        self.raw = rows
        self.np_raw = np.array([[c for c in r] for r in rows])
        self.locked = False

    @property
    def borders(self):
        return {self.left, self.top, self.bottom, self.right,
                self.left[::-1], self.top[::-1], self.bottom[::-1], self.right[::-1]}

    @property
    def top(self):
        return "".join(self.np_raw[0])

    @property
    def bottom(self):
        return "".join(self.np_raw[-1])

    @property
    def left(self):
        return "".join(self.np_raw[:, 0])

    @property
    def right(self):
        return "".join(self.np_raw[:, -1])

    def rotate(self):
        if not self.locked:
            self.np_raw = rot90(self.np_raw)

    def flip(self):
        if not self.locked:
            self.np_raw = flip(self.np_raw, 1)

    def lockit(self):
        self.locked = True


def parse_tiles(data):
    tiles = {}
    cur_tile = []
    cur_tile_id = None
    line = data.pop(0)
    while data:
        if line.startswith('Tile '):
            cur_tile_id = int(line[5:-1])
        elif line == "":
            tiles[cur_tile_id] = Tile(cur_tile)
            cur_tile = []
            cur_tile_id = None
        else:
            cur_tile.append(line)

        line = data.pop(0)

    tiles[cur_tile_id] = Tile(cur_tile)

    return tiles


def flatten(t):
    return [item for sublist in t for item in sublist]


def find_corners(tiles):
    corners = []
    for i, tile in tiles.items():
        other_tiles = [t for k, t in tiles.items() if k != i]
        all_other_borders = flatten([t.borders for t in other_tiles])
        if (tile.top not in all_other_borders and tile.left not in all_other_borders)\
            and (tile.top[::1] not in all_other_borders and tile.left[::-1] not in all_other_borders):
            corners.append(i)
        if (tile.top not in all_other_borders and tile.right not in all_other_borders)\
                and (tile.top[::-1] not in all_other_borders and tile.right[::-1] not in all_other_borders):
            corners.append(i)
        if (tile.bottom not in all_other_borders and tile.left not in all_other_borders)\
                and (tile.bottom[::-1] not in all_other_borders and tile.left[::-1] not in all_other_borders):
            corners.append(i)
        if (tile.bottom not in all_other_borders and tile.right not in all_other_borders)\
                and (tile.bottom[::-1] not in all_other_borders and tile.right[::-1] not in all_other_borders):
            corners.append(i)
    return corners


def part1(data):
    tiles = parse_tiles(data)
    corners = find_corners(tiles)
    return reduce(mul, corners)


DIRECTIONS = {
    'top': (0, -1), 'left': (-1, 0),
    'bottom': (0, 1), 'right': (1, 0)
}

MATCHES = {
    'top': lambda me, other: me.top == other.bottom,
    'bottom': lambda me, other: me.bottom == other.top,
    'left': lambda me, other: me.left == other.right,
    'right': lambda me, other: me.right == other.left,
}


def solve_neighbours(slots, cur_slot, tiles):
    for border, slot in DIRECTIONS.items():
        slot = (cur_slot[0] + slot[0], cur_slot[1] + slot[1])
        if slot not in slots or slots[slot] is not None:
            continue

        my_tile = tiles[slots[cur_slot]]
        possible_tiles = [k for k, t in tiles.items()
                          if k not in slots.values() and len(my_tile.borders.intersection(t.borders)) > 0]

        for k in possible_tiles:
            check_tile = tiles[k]
            rotations = 0
            while not MATCHES[border](my_tile, check_tile) and rotations < 4:
                check_tile.rotate()
                rotations += 1

            if rotations == 4:
                check_tile.flip()
                rotations = 0
                while not MATCHES[border](my_tile, check_tile) and rotations < 4:
                    check_tile.rotate()
                    rotations += 1

            if MATCHES[border](my_tile, check_tile):
                slots[slot] = k
                check_tile.lockit()
                solve_neighbours(slots, slot, tiles)


def find_seamonsters(grid, replace=False):
    sea_monster = [(0,0), (1, 1), (1, 4), (0, 5), (0, 6), (1, 7), (1, 10), (0, 11), (0, 12), (1, 13), (1, 16), (0, 17), (0, 18), (0, 19), (-1, 18)]
    cnt = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            coors = [(x+sm[0], y+sm[1]) for sm in sea_monster]
            if all([(0 <= c[0] < len(grid) and 0 <= c[1] < len(grid) and grid[c[0], c[1]] == '#') for c in coors]):
                cnt += 1
                if replace:
                    for c in coors:
                        grid[c[0], c[1]] = '0'
    return cnt


def part2(data):
    tiles = parse_tiles(data)
    corners = find_corners(tiles)
    tile_count = int(sqrt(len(tiles)))

    slots = {(i, j): None
             for i in range(0, tile_count)
             for j in range(0, tile_count)}

    slots[(0, 0)] = corners[0]

    cur_tile = tiles[corners[0]]
    other_tiles = [t for k, t in tiles.items() if k != corners[0]]
    all_other_borders = flatten([t.borders for t in other_tiles])
    while cur_tile.top in all_other_borders:
        cur_tile.rotate()

    if cur_tile.left in all_other_borders:
        cur_tile.flip()

    solve_neighbours(slots, (0, 0), tiles)

    for cur_slot in slots:
        incorrects = 0
        for border, slot in DIRECTIONS.items():
            slot = (cur_slot[0] + slot[0], cur_slot[1] + slot[1])
            incorrects += 0 if slot not in slots or MATCHES[border](tiles[slots[cur_slot]], tiles[slots[slot]]) else 1
        print(cur_slot, incorrects)

    rows = []
    for y in range(0, tile_count):
        rows.append(np.concatenate([tiles[slots[x, y]].np_raw[1:-1, 1:-1] for x in range(0, tile_count)], axis=1))
    grid = np.concatenate(rows, axis=0)

    rotations = 0
    while find_seamonsters(grid) == 0 and rotations < 8:
        if rotations == 4:
            grid = flip(grid, 1)

        grid = rot90(grid)
        rotations += 1

    find_seamonsters(grid, replace=True)

    return sum([c == '#' for c in grid.flatten()])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 20899048083289
    assert part2(test_1.splitlines()) == 273

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

