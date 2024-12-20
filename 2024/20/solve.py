#!/usr/bin/env python
import heapq
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
                return score + 1, path | {new_pos: score + 1}
            elif new_pos not in path and global_seen[new_pos] > score + 1:
                heapq.heappush(paths, (score + 1, new_pos[0], new_pos[1], path | {new_pos: score + 1}))
                global_seen[new_pos] = score + 1

    return None


def get_next_steps(position):
    return [
        (position[0] + x, position[1] + y) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ]


def get_position_cheats(position, path, grid, max_len):
    to_check = [(1, p[0], p[1], [position]) for p in get_next_steps(position) if grid[p] == "#"]
    cheats = {}
    heapify(to_check)
    global_seen = defaultdict(lambda: 1000000)

    while to_check:
        cheated, cur_x, cur_y, my_path = heapq.heappop(to_check)
        cur_pos = (cur_x, cur_y)
        if grid[cur_pos] == '.':
            cheat_key = (position, cur_pos)
            save_seconds = path[position] - path[cur_pos] - cheated
            if cheat_key not in cheats or cheats[cheat_key] < save_seconds:
                cheats[cheat_key] = save_seconds
            else:
                print(cheats[cheat_key], save_seconds)

        # elif grid[cur_pos] == '#':
        if cheated < max_len:
            for p in get_next_steps(cur_pos):
                if global_seen[p] > cheated + 1:
                    heapq.heappush(to_check, (cheated + 1, p[0], p[1], my_path + [cur_pos]))
                    global_seen[p] = cheated + 1

    return cheats


def get_cheats(path, grid, max_len=2):
    cheats = {}
    for position, score in path.items():
        cheats |= get_position_cheats(position, path, grid, max_len)

    return cheats


def part1(data, save_seconds=100):
    grid, start, end = parse_data(data)
    score, path = get_end_path(grid, start, end)
    cheats = get_cheats(path, grid)

    return len([k for k, v in cheats.items() if v >= save_seconds])


def part2(data, save_seconds=100):
    grid, start, end = parse_data(data)
    score, path = get_end_path(grid, start, end)
    cheats = get_cheats(path, grid, max_len=20)

    print(len([k for k, v in cheats.items() if v >= save_seconds]))
    return len([k for k, v in cheats.items() if v >= save_seconds])


if __name__ == '__main__':

    assert part1(test_1.splitlines(), save_seconds=2) == 44
    assert part1(test_1.splitlines(), save_seconds=20) == 5
    # assert part2(test_1.splitlines(), save_seconds=50) == 285

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

# too low 222879, 956486