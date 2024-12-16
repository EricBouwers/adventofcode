#!/usr/bin/env python
import heapq
from collections import defaultdict
from heapq import heapify

test_1 = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
test_2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""


def parse_data(data):
    maze = {}
    start, end = None, None
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == 'S':
                start = complex(x, y)
                c = '.'
            elif c == 'E':
                end = complex(x, y)
                c = '.'

            maze[complex(x, y)] = c

    return maze, start, end


DIRECTION_TO_STEPS = {
    "N": [('N', -1j, 1), ('E', 0, 1000), ('W', 0, 1000)],
    "E": [('N', 0, 1000), ('E', 1, 1), ('S', 0, 1000)],
    "S": [('E', 0, 1000), ('S', 1j, 1), ('W', 0, 1000)],
    "W": [('N', 0, 1000), ('S', 0, 1000), ('W', -1, 1)],
}


def get_next_steps(cur_pos, facing, maze):
    return [
        (cur_pos + d, f, p) for f, d, p in DIRECTION_TO_STEPS[facing] if maze[cur_pos + d] != '#'
    ]


def get_end_paths(maze, start, end):
    paths = [(0, (start.real, start.imag), 'E', [(start, 'E')])]
    heapify(paths)
    ends = []
    global_seen = defaultdict(lambda: 1000000)
    all_path = defaultdict(lambda: list())

    while paths:
        score, cur_pos, facing, seen = heapq.heappop(paths)
        cur_pos = complex(cur_pos[0], cur_pos[1])
        for p, d, s in get_next_steps(cur_pos, facing, maze):
            new_score = score + s
            if p == end:
                ends.append((new_score, p, d, seen + [(p, d)]))
            elif (p, d) not in seen and global_seen[(p, d)] > new_score:
                heapq.heappush(paths, (new_score, (p.real, p.imag), d, seen + [(p, d)]))
                global_seen[(p, d)] = new_score
            elif global_seen[(p, d)] == new_score:
                all_path[(p, d)].extend(seen)

    return ends, all_path


def part1(data):
    maze, start, end = parse_data(data)
    return min([e[0] for e in get_end_paths(maze, start, end)[0]])


def print_grid(grid, all_paths, data):
    for y in range(len(data)):
        line = ""
        for x in range(len(data[0])):
            coor = complex(x, y)
            line += '*' if (grid[coor] == '#' and coor in all_paths) else "#" if grid[coor] == '#' else 'O' if coor in all_paths else '.'

        print(line)


def part2(data):
    maze, start, end = parse_data(data)
    all_pos = set()
    end_paths, all_paths = get_end_paths(maze, start, end)
    best_score = min([e[0] for e in end_paths])

    for end_path in [e for e in end_paths if e[0] == best_score]:
        for p_d in end_path[3]:
            all_pos.add(p_d)

    updated_all_pos = set()
    old_len = len(all_pos)
    new_len = 0
    while old_len != new_len:
        old_len = len(all_pos)
        updated_all_pos.update(all_pos)
        for pos in all_pos:
            for path in all_paths[pos]:
                updated_all_pos.add(path)
        all_pos = set(updated_all_pos)
        new_len = len(all_pos)

    return len(set([x[0] for x in all_pos]))


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 7036
    assert part1(test_2.splitlines()) == 11048
    assert part2(test_1.splitlines()) == 45
    assert part2(test_2.splitlines()) == 64

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
