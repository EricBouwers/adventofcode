#!/usr/bin/env python
import heapq
import itertools
from collections import defaultdict
from heapq import heapify

test_1 = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""
test_2 = """"""


def parse_data(data):
    grid = defaultdict(lambda: "#")
    start, end = None, None
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == 'S':
                start = (x, y)
                c = '.'
            if c == 'E':
                end = (x, y)
                c = '.'
            grid[(x, y)] = c

    return grid, start, end


def get_end_path(grid, start, end):
    paths = [(0, start[0], start[1], {start: 0})]
    heapify(paths)
    global_seen = defaultdict(lambda: 1000000)

    while paths:
        score, cur_x, cur_y, path = heapq.heappop(paths)
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (cur_x + x, cur_y + y)
            if grid[new_pos] == "#":
                continue
            elif new_pos == end:

                return score + 1, {complex(p[0], p[1]): s for p, s in (path | {new_pos: score + 1}).items()}
            elif new_pos not in path and global_seen[new_pos] > score + 1:
                heapq.heappush(paths, (score + 1, new_pos[0], new_pos[1], path | {new_pos: score + 1}))
                global_seen[new_pos] = score + 1

    return None


def get_check_cross(max_cheats):
    cross = set()
    for x in range(max_cheats + 1):
        cross.add((complex(x, 0), x))
        cross.add((complex(-x, 0), x))
        cross.add((complex(0, x), x))
        cross.add((complex(0, -x), x))
        for y in range(max_cheats - x + 1):
            cross.add((complex(x, y), x + y))
            cross.add((complex(-x, y), x + y))
            cross.add((complex(-x, -y), x + y))
            cross.add((complex(y, x), x + y))
            cross.add((complex(y, -x), x + y))
            cross.add((complex(-y, -x), x + y))

    return [x for x in cross if x != complex(0, 0)]


def get_position_cheats_cross(position, path, cross):
    cheats = []
    for add, cheated in cross:
        new_pos = position + add
        if new_pos in path:
            cheat_key = (position, new_pos)
            save_seconds = path[position] - path[new_pos] - cheated
            cheats.append(save_seconds)

    return cheats


def get_cheats(path, max_len=2):
    cheats = []
    check_cross = get_check_cross(max_len)
    for position, score in path.items():
        cheats.extend(get_position_cheats_cross(position, path, check_cross))

    return cheats


def part1(data, save_seconds=100):
    grid, start, end = parse_data(data)
    score, path = get_end_path(grid, start, end)
    cheats = get_cheats(path)

    return len([v for v in cheats if v >= save_seconds])


def part2(data, save_seconds=100):
    grid, start, end = parse_data(data)
    score, path = get_end_path(grid, start, end)
    cheats = get_cheats(path, max_len=20)

    return len([v for v in cheats if v >= save_seconds])


if __name__ == '__main__':

    assert part1(test_1.splitlines(), save_seconds=2) == 44
    assert part1(test_1.splitlines(), save_seconds=20) == 5
    assert part2(test_1.splitlines(), save_seconds=50) == 285

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
