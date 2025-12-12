#!/usr/bin/env python
from copy import deepcopy
from heapq import heapify, heappush, heappop

test_1 = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""
test_2 = """"""


def parse_data(data):
    piece_id = None
    piece_y = 0
    puzzle_piece = {}
    pieces = []
    puzzle_boards = []
    for d in data:
        if d == "":
            pass
        elif d[1] == ":":
            if piece_id is not None:
                pieces.append(puzzle_piece)

            piece_id = int(d[0])
            piece_y = 0
            puzzle_piece = {}
        elif "#" in d:
            for x, c in enumerate(d):
                puzzle_piece[(x, piece_y)] = 0 if c == "." else 1
            piece_y += 1
        elif "x" in d:
            parts = d.split(" ")
            puzzle_boards.append((tuple(map(int,parts[0].replace(":","").split("x"))), list(map(int, parts[1:]))))

    pieces.append(puzzle_piece)

    return pieces, puzzle_boards


def place_piece(coordinate, board, piece):
    new_board = deepcopy(board)
    for p, piece_c in [((coordinate[0] + piece_c[0], coordinate[1] + piece_c[1]), piece_c) for piece_c in piece]:
        if piece[piece_c] == 1:
            if p not in new_board or new_board[p] > 0:
                return None
            else:
                new_board[p] = piece[piece_c]
    return new_board


def get_new_states(dimensions, board, pieces):
    new_states = []
    for piece in pieces:
        for y in range(0, dimensions[0]):
            for x in range(0, dimensions[1]):
                new_board = place_piece((x,y), board, piece)
                if new_board is not None:
                    new_states.append(new_board)

    return new_states


def get_state_key(dimensions, state, wanted):
    key = ""
    for y in range(0, dimensions[0]):
        line = ""
        for x in range(0, dimensions[1]):
            line += str(state[(x, y)])
        key += ",line"
    key += "_" + "__".join(map(str,wanted))

    return key


def is_possible(dimensions, wanted, pieces):
    start_board = {(x,y): 0 for x in range(0, dimensions[1]) for y in range(0, dimensions[0])}
    states = [(start_board, wanted)]
    seen_states = set()

    while states:
        board, wanted = states.pop()

        for i, w in enumerate(wanted):
            if w > 0:
                new_states = get_new_states(dimensions, board, pieces[i])
                if new_states:
                    new_wanted = [w if i != j else w-1 for j, w in enumerate(wanted)]
                    if sum(new_wanted) == 0:
                        return True
                    else:
                        for s in new_states:
                            state_key = get_state_key(dimensions, s, new_wanted)
                            if state_key not in seen_states:
                                seen_states.add(state_key)
                                states.append((s, new_wanted))

    return False


def part1(data):
    pieces, puzzle_boards = parse_data(data)
    piece_blocks_needed = [sum(p.values()) for p in pieces]

    pieces_with_rotations = []
    for i, p in enumerate(pieces):
        pieces_with_rotations.append([])
        matrix_piece = []
        for y in range(0, 3):
            row = []
            for x in range(0, 3):
                row.append(p[(x, y)])
            matrix_piece.append(row)
        pieces_with_rotations[i] = [p]
        for r in range(0, 3):
            matrix_piece = list(zip(*matrix_piece))[::-1]
            pieces_with_rotations[i].append({(x, y): matrix_piece[y][x] for x in range(0, 3) for y in range(0, 3)})

    possible_boards, impossible_boards, easy_boards = [], [], []
    for dimensions, wanted in puzzle_boards:
        total_blocks_available = dimensions[0] * dimensions[1]
        total_blocks_needed = sum([w * piece_blocks_needed[i] for i, w in enumerate(wanted)])
        easy_fit = sum([w * 9 for w in wanted])

        if total_blocks_needed > total_blocks_available:
            impossible_boards.append((dimensions, wanted))
        elif total_blocks_available >= easy_fit:
            easy_boards.append((dimensions, wanted))
        else:
            if is_possible(dimensions, wanted, pieces_with_rotations):
                possible_boards.append((dimensions, wanted))
            else:
                impossible_boards.append((dimensions, wanted))

    return len(easy_boards) + len(possible_boards)


def part2(data):
    parsed = parse_data(data)
    return None


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 2
    assert part2(test_1.splitlines()) == None

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
