#!/usr/bin/env python
from collections import defaultdict

test_1 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
test_2 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""
test_3 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""


def parse_data(data):
    grid = defaultdict(lambda: '#')
    moves = []
    for y, l in enumerate(data):
        if l:
            for x, c in enumerate(l):
                if c == '<':
                    moves.append(-1)
                elif c == '>':
                    moves.append(1)
                elif c == '^':
                    moves.append(-1j)
                elif c == 'v':
                    moves.append(1j)
                else:
                    grid[complex(x, y)] = c

    return grid, moves


def get_line_to_move(robot, move, boxes, grid):
    next_pos = robot + move

    if grid[next_pos] == '#':
        return [], False
    else:
        if next_pos in boxes:
            boxes_to_move, can_move = get_line_to_move(next_pos, move, boxes, grid)
            boxes_to_move.append(next_pos)
            return boxes_to_move, can_move
        else:
            return [], True


def get_structure_to_move(robot, move, boxes, grid):
    next_pos = robot + move

    if grid[next_pos] == '#':
        return [], False
    else:
        if next_pos in boxes:
            if move.imag == 0:
                boxes_to_move, can_move = get_structure_to_move(next_pos, move, boxes, grid)
                boxes_to_move.append(next_pos)
            else:
                if boxes[next_pos] == ']':
                    other_next_pos = next_pos - 1
                else:
                    other_next_pos = next_pos + 1
                boxes_to_move_right, can_move_left = get_structure_to_move(next_pos, move, boxes, grid)
                boxes_to_move_left, can_move_right = get_structure_to_move(other_next_pos, move, boxes, grid)

                boxes_to_move = boxes_to_move_left + boxes_to_move_right + [next_pos, other_next_pos]
                can_move = can_move_left and can_move_right

            return boxes_to_move, can_move
        else:
            return [], True


def part1(data):
    grid, moves = parse_data(data)
    robot = [c for c in grid.keys() if grid[c] == '@'][0]
    boxes = [c for c in grid.keys() if grid[c] == 'O']

    for m in moves:
        boxes_to_move, can_move = get_line_to_move(robot, m, boxes, grid)
        if can_move:
            robot += m
            boxes = [b for b in boxes if b not in boxes_to_move]
            boxes.extend([b + m for b in boxes_to_move])

    return sum([100 * int(b.imag) + int(b.real) for b in boxes])


def part2(data):
    data = [d.replace('#', '##') for d in data]
    data = [d.replace('.', '..') for d in data]
    data = [d.replace('O', '[]') for d in data]
    data = [d.replace('@', '@.') for d in data]

    grid, moves = parse_data(data)
    robot = [c for c in grid.keys() if grid[c] == '@'][0]
    boxes = {c: grid[c] for c in grid.keys() if grid[c] in '[]'}

    for m in moves:
        boxes_to_move, can_move = get_structure_to_move(robot, m, boxes, grid)
        if can_move:
            robot += m
            new_boxes = {}
            for b, v in boxes.items():
                if b in boxes_to_move:
                    new_boxes[b + m] = v
                else:
                    new_boxes[b] = v
            boxes = new_boxes

    return sum([100 * int(b.imag) + int(b.real) for b, v in boxes.items() if v == '['])


if __name__ == '__main__':

    assert part1(test_2.splitlines()) == 2028
    assert part1(test_1.splitlines()) == 10092
    assert part2(test_3.splitlines()) > 0
    assert part2(test_1.splitlines()) == 9021

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

