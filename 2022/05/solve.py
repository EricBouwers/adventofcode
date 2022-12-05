#!/usr/bin/env python

from collections import defaultdict

test_1 = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
test_2 = """"""


def parse_data(data):
    crates = defaultdict(list)
    moves = []

    for d in data:
        if d.startswith('move'):
            m = d.split(" ")
            moves.append([int(m[1]), int(m[3]), int(m[5])])
        elif '[' in d:
            for i, x in enumerate(range(0, len(d), 4)):
                if d[x] == '[':
                    crates[i+1].append(d[x+1])

    for v in crates.values():
        v.reverse()

    return crates, moves


def part1(data):
    crates, moves = parse_data(data)

    for move in moves:
        for m in range(0, move[0]):
            crates[move[2]].append(crates[move[1]].pop())

    highest = ""
    for i in range(1, max(crates.keys())+1):
        highest += crates[i].pop()

    return highest


def part2(data):
    crates, moves = parse_data(data)

    for move in moves:
        crates[move[2]] = crates[move[2]] + crates[move[1]][-move[0]:]
        crates[move[1]] = crates[move[1]][0:len(crates[move[1]])-move[0]]

    highest = ""
    for i in range(1, max(crates.keys())+1):
        highest += crates[i].pop()

    return highest


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == "CMZ"
    assert part2(test_1.splitlines()) == "MCD"

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

