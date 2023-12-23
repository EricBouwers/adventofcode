#!/usr/bin/env python
import heapq
from collections import defaultdict
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


def print_path(path, grid, max_y, max_x):
    for y in range(0, max_y):
        line = ''
        for x in range(0, max_x):
            line += '0' if (x, y) in path else grid[(x, y)]
        print(line)


def condens(grid, from_to):
    for p, c in grid.items():
        if c != '#':
            from_to[p] = set([(p, 1) for p in possible_steps(p, grid, True)])

    prev_len = 0
    while len(from_to) != prev_len:
        prev_len = len(from_to)
        to_del = []
        for k, v in from_to.items():
            if len(v) == 2:
                f, t = v
                from_to[f[0]].remove((k, f[1]))
                from_to[t[0]].remove((k, t[1]))
                from_to[f[0]].add((t[0], t[1] + f[1]))
                from_to[t[0]].add((f[0], t[1] + f[1]))
                to_del.append(k)
        for k in to_del:
            del from_to[k]


def find_hikes(data):
    grid, start, end = parse_data(data)

    paths = [(start, set())]
    heapify(paths)
    visited_paths = {}

    while paths:
        cur_pos, seen = heapq.heappop(paths)
        for poss in possible_steps(cur_pos, grid, False):
            if poss not in seen:
                visited_paths[poss] = seen if poss not in visited_paths or len(seen) > len(visited_paths[poss]) else visited_paths[poss]
                heapq.heappush(paths, (poss, seen | {cur_pos}))

    return visited_paths[end]


def part1(data):
    path = find_hikes(data)
    return len(path) + 1


def part2(data):
    grid, start, end = parse_data(data)

    from_to = defaultdict(lambda: set())
    condens(grid, from_to)

    paths = [(start, set(), 0)]
    visited_paths = {}

    while paths:
        cur_pos, seen, to_me = paths.pop()
        for poss, to_poss in from_to[cur_pos]:
            path_len = to_me + to_poss
            if poss not in seen:
                visited_paths[poss] = path_len if poss not in visited_paths or path_len > visited_paths[poss] else visited_paths[poss]
                paths.append((poss, seen | {cur_pos}, path_len))

    return visited_paths[end]


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 94
    assert part2(test_1.splitlines()) == 154

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

# too low 4886, 4887, 5306 also too low

# 5586, 5722
# 6682