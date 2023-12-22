#!/usr/bin/env python
from itertools import combinations

test_1 = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""
test_2 = """"""


class Cube:

    def __init__(self, coordinates, name):
        self.name = name
        self.coordinates = coordinates
        self.supports = []
        self.supported_by = []

        self.xy_coords = set()
        for x in range(min(self.xs()), max(self.xs()) + 1):
            for y in range(min(self.ys()), max(self.ys()) + 1):
                self.xy_coords.add((x, y))

        self.supporting_nodes = None

    def intersect(self, other):
        return self.coordinates[2] <= other.coordinates[5] and other.coordinates[2] <= self.coordinates[5] and \
               self.coordinates[1] <= other.coordinates[4] and other.coordinates[1] <= self.coordinates[4] and \
               self.coordinates[0] <= other.coordinates[3] and other.coordinates[0] <= self.coordinates[3]

    def lower(self):
        return Cube([j - (1 if i in [2, 5] else 0) for i, j in enumerate(self.coordinates)], self.name)

    def xs(self):
        return [self.coordinates[0], self.coordinates[3]]

    def ys(self):
        return [self.coordinates[1], self.coordinates[4]]

    def lowestZ(self):
        return min([self.coordinates[2], self.coordinates[5]])

    def can_be_disintegrated(self):
        return all([len([s for s in supported.supported_by if s != self]) > 0 for supported in self.supports])

    def __repr__(self):
        return str(self.name) + ' ' + str(self.coordinates) + ', supports:' + ';'.join([c.name for c in self.supports])


def parse_data(data):
    cubes = [Cube([int(c) for c in line.replace("~", ',').split(',')], str(n)) for n, line in enumerate(data)]
    cubes.sort(key=lambda x: x.lowestZ())
    return cubes


def fall_cubes(cubes):
    fallen_cubes = 0
    max_x = max([max(c.xs()) for c in cubes])
    max_y = max([max(c.ys()) for c in cubes])
    min_x = min([min(c.xs()) for c in cubes])
    min_y = min([min(c.ys()) for c in cubes])
    ground = Cube([min_x, min_y, 0, max_x, max_y, 0], 'ground')

    stable = [ground]
    to_go = [c for c in cubes]
    added = True
    while added:
        added = False
        still_to_go = []
        for cube in to_go:
            lowered_cube = cube.lower()
            supported_by = [c for c in stable if c.intersect(lowered_cube)]
            if len(supported_by) > 0:
                stable.append(cube)
                added = True
                for c in supported_by:
                    c.supports.append(cube)
            else:
                still_to_go.append(cube)
        to_go = still_to_go

    while to_go:
        still_to_go = []
        for cube in map(lambda c: c.lower(), to_go):
            lowered_cube = cube.lower()
            supported_by = [c for c in stable if c.intersect(lowered_cube)]
            if len(supported_by) > 0:
                stable.append(cube)
                for c in supported_by:
                    c.supports.append(cube)
                    cube.supported_by.append(c)
                fallen_cubes += 1
            else:
                still_to_go.append(cube)
        to_go = still_to_go

    return stable, ground, fallen_cubes


def part1(data):
    cubes = parse_data(data)

    stable, _, _ = fall_cubes(cubes)
    return sum([c.can_be_disintegrated() for c in stable])


def part2(data):
    cubes = parse_data(data)
    stable, ground, _ = fall_cubes(cubes)

    total = 0
    for i, c in enumerate([s for s in stable if not s.can_be_disintegrated()]):
        new_cubes = [b for b in stable if b != ground and b != c]
        _, _, fallen = fall_cubes(new_cubes)
        if fallen:
            total += fallen

    return total


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 5
    assert part2(test_1.splitlines()) == 7

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

