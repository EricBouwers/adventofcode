#!/usr/bin/env python
from collections import defaultdict

test_1 = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""
test_2 = """"""


def parse_data(data):
    board = defaultdict(lambda: " ")
    steps = []
    start = None
    for y, d in enumerate(data):
        if '.' in d:
            for x, c in enumerate(d):
                board[(x, y)] = c
                start = start if start is not None else (x, y) if c == '.' else None
        elif 'R' in d:
            d = d.replace("R", " R ").replace("L", " L ")
            steps = [int(i) if i.isdigit() else i for i in d.split(" ")]

    return steps, start, board


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def take_wrap_step(cur_pos, cur_dir, board):
    new_pos = (cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1])
    if board[new_pos] == '.':
        return new_pos, cur_dir
    elif board[new_pos] == '#':
        return cur_pos, cur_dir
    elif board[new_pos] == ' ':
        new_pos = cur_pos
        while board[new_pos] != " ":
            new_pos = (new_pos[0] - cur_dir[0], new_pos[1] - cur_dir[1])
        newer_pos, _ = take_wrap_step(new_pos, cur_dir, board)
        return (newer_pos, cur_dir) if newer_pos != new_pos else (cur_pos, cur_dir)


def take_cube_step(specials):
    def take_step(cur_pos, cur_dir, board):
        new_pos = (cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1])
        if (new_pos, cur_dir) in specials:
            return specials[(new_pos, cur_dir)] if board[specials[(new_pos, cur_dir)][0]] != "#" else (cur_pos, cur_dir)
        elif board[new_pos] == '.':
            return new_pos, cur_dir
        elif board[new_pos] == '#':
            return cur_pos, cur_dir
        elif board[new_pos] == ' ':
            return specials[(new_pos, cur_dir)] #if board[specials[new_pos][0]] != "#" else (cur_pos, cur_dir)
    return take_step


def walk_board(data, step_func):
    steps, start, board = parse_data(data)

    cur_pos = start
    cur_dir = (1, 0)

    for step in steps:
        if step == "R":
            cur_dir = DIRECTIONS[(DIRECTIONS.index(cur_dir) + 1) % 4]
        elif step == 'L':
            cur_dir = DIRECTIONS[DIRECTIONS.index(cur_dir) - 1]
        else:
            for i in range(0, int(step)):
                cur_pos, cur_dir = step_func(cur_pos, cur_dir, board)

    return 1000 * (cur_pos[1] + 1) + 4 * (cur_pos[0] + 1) + DIRECTIONS.index(cur_dir)


def part1(data):
    return walk_board(data, take_wrap_step)


def part2(data, size=50):
    if size == 4:
        specials = {
            ((12, 0), (1, 0)): ((15, 11), (-1, 0)),
            ((12, 1), (1, 0)): ((14, 11), (-1, 0)),
            ((7, 0), (-1, 0)): ((4, 4), (0, -1)),
            ((7, 1), (-1, 0)): ((5, 4), (0, -1)),
            ((7, 2), (-1, 0)): ((6, 4), (0, -1)),
            ((7, 3), (-1, 0)): ((7, 4), (0, -1)),
            ((12, 4), (1, 0)): ((15, 8), (0, 1)),
            ((12, 5), (1, 0)): ((14, 8), (0, 1)),
            ((12, 6), (1, 0)): ((13, 8), (0, 1)),
            ((12, 7), (1, 0)): ((12, 8), (0, 1)),
            ((8, 12), (0, 1)): ((3, 7), (0, -1)),
            ((9, 12), (0, 1)): ((2, 7), (0, -1)),
            ((10, 12), (0, 1)): ((1, 7), (0, -1)),
            ((11, 12), (0, 1)): ((0, 7), (0, -1)),
            ((6, 3), (0, -1)): ((8, 2), (1, 0))
        }
    else:
        specials = {}
        specials = {**specials, **{((i, -1), (0, -1)): ((0, 150+i-50), (1, 0)) for i in range(50, 100)}}  # top 1
        specials = {**specials, **{((-1, i), (-1, 0)): ((50 + i - 150, 0), (0, 1)) for i in range(150, 200)}}  # left 6
        specials = {**specials, **{((i, 150), (0, 1)): ((49, 150 + i - 50), (-1, 0)) for i in range(50, 100)}}  # bottom 4
        specials = {**specials, **{((50, i), (1, 0)): ((i-100, 149), (0, -1)) for i in range(150, 200)}}  # right 6
        specials = {**specials, **{((i, 99), (0, -1)): ((50, 50+i), (1, 0)) for i in range(0, 50)}}  # top 5
        specials = {**specials, **{((49, i), (-1, 0)): ((i-50, 100), (0, 1)) for i in range(50, 100)}}  # left 3
        specials = {**specials, **{((i, 200), (0, 1)): ((100+i, 0), (0, 1)) for i in range(0, 50)}}  # bottom 6
        specials = {**specials, **{((i, -1), (0, -1)): ((i - 100, 199), (0, -1)) for i in range(100, 150)}}  # top 2
        specials = {**specials, **{((49, i), (-1, 0)): ((0, 149-i), (1, 0)) for i in range(0, 50)}}  # left 1
        specials = {**specials, **{((-1, i), (-1, 0)): ((50, 149-i), (1, 0)) for i in range(100, 150)}}  # left 5
        specials = {**specials, **{((150, i), (1, 0)): ((99, 149-i), (-1, 0)) for i in range(0, 50)}}  # right 2
        specials = {**specials, **{((100, i), (1, 0)): ((149, abs(i - 149)), (-1, 0)) for i in range(100, 150)}}  # right 4
        specials = {**specials, **{((100, i), (1, 0)): ((100 + i - 50, 49), (0, -1)) for i in range(50, 100)}}  # right 3
        specials = {**specials, **{((i, 50), (0, 1)): ((99, 50 + i - 100), (-1, 0)) for i in range(100, 150)}}  # bottom 2

        # Yes, for validating the specials :(
        # steps, start, board = parse_data(data)
        #
        # # check specials with turnaround, step, turnaround step should come in same position
        # step_func = take_cube_step(specials)
        # print(len(specials))
        # for k, val in specials.items():
        #
        #     cur_pos, cur_dir = val
        #     for step in ["R", "R", "1", "R", "R", "1"]:
        #         if step == "R":
        #             cur_dir = DIRECTIONS[(DIRECTIONS.index(cur_dir) + 1) % 4]
        #         elif step == 'L':
        #             cur_dir = DIRECTIONS[DIRECTIONS.index(cur_dir) - 1]
        #         else:
        #             for i in range(0, int(step)):
        #                 cur_pos, cur_dir = step_func(cur_pos, cur_dir, board)
        #     if cur_pos != val[0] or cur_dir != val[1]:
        #         print("wrong!", k, val, cur_pos, cur_dir, cur_pos != val[0], cur_dir != val[1])

    return walk_board(data, take_cube_step(specials))


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 6032
    assert part2(test_1.splitlines(), 4) == 5031

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
