#!/usr/bin/env python
import operator
from collections import defaultdict

test_1 = """AAAA
BBCD
BBCC
EEEC
"""
test_2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""
test_3 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
test_4 = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""
test_5 = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""


def parse_data(data):
    grid = {}
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            grid[(x, y)] = c
    return grid


def take_step(pos, d):
    return tuple([operator.add(*x) for x in zip(pos, d)])


def get_diagonal_neighbours(position, value, grid):
    neighbours = []
    for d in [(1, 1), (-1, -1), (-1, 1), (1, -1)]:
        new_pos = take_step(position, d)
        if new_pos in grid and grid[new_pos] == value:
            neighbours.append(new_pos)

    return neighbours


def get_neighbours(position, value, grid):
    neighbours = []
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_pos = take_step(position, d)
        if new_pos in grid and grid[new_pos] == value:
            neighbours.append(new_pos)

    return neighbours


def get_region(start, region_id, grid):
    coordinates = {start}
    to_check = [start]
    while to_check:
        pos = to_check.pop()
        candidates = get_neighbours(pos, region_id, grid)
        to_check.extend([c for c in candidates if c not in coordinates])
        coordinates.update(candidates)

    return coordinates


def parse_regions(grid):
    regions = defaultdict(list)
    seen = set()
    for c in grid.keys():
        if c not in seen:
            region_id = grid[c]
            region_coordinates = get_region(c, region_id, grid)
            regions[region_id].append(region_coordinates)
            seen.update(region_coordinates)

    return regions


def get_perimeter(region, id, grid):
    return sum([4 - len(get_neighbours(plant, id, grid)) for plant in region])


def get_corners(plant, neighbours, id, grid):
    if len(neighbours) == 0:
        return 4
    elif len(neighbours) == 1:
        return 2
    elif len(neighbours) == 2:
        if neighbours[0][0] == neighbours[1][0] or neighbours[0][1] == neighbours[1][1]:
            return 0  # straight line
        else:
            n1 = get_neighbours(neighbours[0], id, grid)
            n2 = get_neighbours(neighbours[1], id, grid)
            return 1 if len(set(n1).intersection(set(n2))) > 1 else 2
    elif len(neighbours) == 3:
        return sum([1 if get_corners(plant, combo, id, grid) == 2 else 0 for combo in [
            [neighbours[0], neighbours[1]],
            [neighbours[0], neighbours[2]],
            [neighbours[1], neighbours[2]],
        ]])
    else:
        return 4 - len(get_diagonal_neighbours(plant, id, grid))


def get_sides(region, id, grid):
    corners = 0
    for plant in region:
        neighbours = get_neighbours(plant, id, grid)
        corners += get_corners(plant, neighbours, id, grid)

    return corners


def part1(data):
    grid = parse_data(data)
    regions = parse_regions(grid)

    costs = 0
    for id, plants in regions.items():
        for p in plants:
            costs += len(p) * get_perimeter(p, id, grid)

    return costs


def part2(data):
    grid = parse_data(data)
    regions = parse_regions(grid)

    costs = 0
    for id, plants in regions.items():
        for p in plants:
            costs += len(p) * get_sides(p, id, grid)

    return costs


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 140
    assert part1(test_2.splitlines()) == 772
    assert part1(test_3.splitlines()) == 1930
    assert part2(test_1.splitlines()) == 80
    assert part2(test_4.splitlines()) == 236
    assert part2(test_5.splitlines()) == 368
    assert part2(test_3.splitlines()) == 1206

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

