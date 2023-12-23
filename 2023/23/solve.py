#!/usr/bin/env python
import heapq
from heapq import heapify

test_1 = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
test_2 = """"""


def parse_data(data):
    grid = {}
    start = None
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            grid[(x, y)] = c
            if start is None and y == 0 and c == '.':
                start = (x, y)

    end = None
    for x, c in enumerate(data[-1]):
        if c == '.':
            end = (x, len(data) - 1)

    return grid, start, end


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

NEXT_DIRS = {
    '.': [UP, DOWN, LEFT, RIGHT],
    '>': [RIGHT],
    '<': [LEFT],
    '^': [UP],
    'v': [DOWN],
}


def take_step(dir, pos):
    return pos[0] + dir[0], pos[1] + dir[1]


def possible_steps(cur_pos, grid, can_slope):
    directions = NEXT_DIRS['.'] if can_slope else NEXT_DIRS[grid[cur_pos]]
    return [pos for pos in map(lambda d: take_step(d, cur_pos), directions) if pos in grid and grid[pos] != '#']


def find_hikes(data, can_slope=False):
    grid, start, end = parse_data(data)

    paths = [(start, set())]
    heapify(paths)
    visited_paths = {}

    while paths:
        cur_pos, seen = heapq.heappop(paths)
        seen.add(cur_pos)
        for poss in possible_steps(cur_pos, grid, can_slope):
            if poss not in seen and (poss not in visited_paths or len(visited_paths[poss]) <= len(seen)):
                visited_paths[poss] = seen
                heapq.heappush(paths, (poss, set(seen)))

    return visited_paths[end]


def part1(data):
    path = find_hikes(data, False)
    return len(path)


def part2(data):
    path = find_hikes(data, True)
    return len(path)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 94
    assert part2(test_1.splitlines()) == 154

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

# too low 4886, 4887, 5306 also too low

# 5586
# 6682