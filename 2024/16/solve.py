#!/usr/bin/env python
from collections import defaultdict

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
    "N": [('N', -1j, 0), ('E', 1, 1000), ('S', 1j, 2000), ('W', -1, 1000)],
    "E": [('N', -1j, 1000), ('E', 1, 0), ('S', 1j, 1000), ('W', -1, 2000)],
    "S": [('N', -1j, 2000), ('E', 1, 1000), ('S', 1j, 0), ('W', -1, 1000)],
    "W": [('N', -1j, 1000), ('E', 1, 2000), ('S', 1j, 1000), ('W', -1, 0)],
}


def get_next_steps(cur_pos, facing, maze):
    return [
        (cur_pos + d, f, p) for f, d, p in DIRECTION_TO_STEPS[facing] if maze[cur_pos + d] != '#'
    ]


def get_end_paths(maze, start, end):
    paths = [(start, 'E', 0, set())]
    ends = []
    global_seen = defaultdict(lambda: 1000000)

    while paths:
        cur_pos, facing, score, seen = paths.pop(0)
        for p, d, s in get_next_steps(cur_pos, facing, maze):
            new_score = score + s + 1
            if p == end:
                ends.append((p, d, new_score, seen | {p}))
            elif p not in seen and global_seen[(p, d)] > new_score:
                paths.append((p, d, new_score, seen | {cur_pos}))
                global_seen[(p, d)] = new_score

    return ends


def part1(data):
    maze, start, end = parse_data(data)
    return min([e[2] for e in get_end_paths(maze, start, end)])


def part2(data):
    maze, start, end = parse_data(data)
    all_pos = set()
    end_paths = get_end_paths(maze, start, end)
    best_score = min([e[2] for e in end_paths])

    for end_path in [e for e in end_paths if e[2] == best_score]:
        all_pos.update(end_path[3])

    print(len(all_pos), all_pos)
    return len(all_pos)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 7036
    assert part1(test_2.splitlines()) == 11048
    # assert part2(test_1.splitlines()) == 45
    # assert part2(test_1.splitlines()) == 64

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

