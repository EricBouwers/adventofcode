#!/usr/bin/env python
from collections import defaultdict

test_1 = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

MOVES = {
    'e': lambda c: (c[0]+1, c[1]-1, c[2]),
    'se': lambda c: (c[0], c[1]-1, c[2]+1),
    'sw': lambda c: (c[0]-1, c[1], c[2]+1),
    'w': lambda c: (c[0]-1, c[1]+1, c[2]),
    'nw': lambda c: (c[0], c[1]+1, c[2]-1),
    'ne': lambda c: (c[0]+1, c[1], c[2]-1),
}


def parse_coor(line):
    coor = (0, 0, 0)
    while line:
        if line[0:2] in ['se', 'sw', 'nw', 'ne']:
            dir = line[0:2]
            line = line[2:]
        else:
            dir = line[0]
            line = line[1:]
        coor = MOVES[dir](coor)

    return coor


def part1(data):
    tiles = defaultdict(lambda: 0)
    for line in data:
        coor = parse_coor(line)
        tiles[coor] = 1 if tiles[coor] == 0 else 0

    return sum(tiles.values())


def part2(data):
    tiles = defaultdict(lambda: 0)
    for line in data:
        coor = parse_coor(line)
        tiles[coor] = 1 if tiles[coor] == 0 else 0

    for _ in range(0, 100):
        new_tiles = defaultdict(lambda: 0)
        to_consider = set()
        for tile in [c for c, t in tiles.items() if t == 1]:
            neighbours = [move(tile) for move in MOVES.values()]
            sum_neighbours = sum([tiles[n] for n in neighbours])
            if sum_neighbours == 0 or sum_neighbours > 2:
                new_tiles[tile] = 0
            else:
                new_tiles[tile] = 1
            to_consider.update(neighbours)

        for tile in [t for t in to_consider if tiles[t] == 0]:
            neighbours = [move(tile) for move in MOVES.values()]
            sum_neighbours = sum([tiles[n] for n in neighbours])
            if sum_neighbours == 2:
                new_tiles[tile] = 1
            else:
                new_tiles[tile] = 0

        tiles = new_tiles

    return sum(tiles.values())


if __name__ == '__main__':

    print(parse_coor('nwwswee'))
    assert part1(test_1.splitlines()) == 10
    assert part2(test_1.splitlines()) == 2208

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

