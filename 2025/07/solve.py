#!/usr/bin/env python
from collections import defaultdict

test_1 = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
test_2 = """"""


def parse_data(data):
    grid = defaultdict(lambda: None)
    s_pos = None

    for y, d in enumerate(data):
        for x, c in enumerate(d):
            grid[(x,y)] = c
            if c == 'S':
                s_pos = (x,y)

    return grid, s_pos, len(data[0]), len(data[y])


def part1(data):
    grid, s_pos, max_x, max_y = parse_data(data)

    beams = {s_pos}
    cur_y = s_pos[1]
    splits = 0
    while cur_y < max_y:
        new_beams = set()
        for beam in beams:
            new_beam_point = (beam[0], beam[1]+1)
            if grid[new_beam_point] == '^':
                new_beams.add((beam[0] - 1, beam[1] + 1))
                new_beams.add((beam[0] + 1, beam[1] + 1))
                splits += 1
            elif grid[new_beam_point] == '.':
                new_beams.add(new_beam_point)
        beams = new_beams
        cur_y += 1

    return splits


def part2(data):
    grid, s_pos, max_x, max_y = parse_data(data)

    beams = {s_pos: 1}
    cur_y = s_pos[1]
    while cur_y < max_y:
        new_beams = defaultdict(lambda: 0)
        for beam, timelines in beams.items():
            new_beam_point = (beam[0], beam[1]+1)
            if grid[new_beam_point] == '^':
                new_beams[(beam[0] - 1, beam[1] + 1)] += timelines
                new_beams[(beam[0] + 1, beam[1] + 1)] += timelines
            elif grid[new_beam_point] == '.':
                new_beams[new_beam_point] += timelines
        beams = new_beams
        cur_y += 1

    return sum(beams.values())


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 21
    assert part2(test_1.splitlines()) == 40

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

