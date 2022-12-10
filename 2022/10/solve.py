#!/usr/bin/env python
from collections import defaultdict

test_1 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
test_2 = """"""


def parse_data(data):
    instructions = []
    for d in data:
        if d != 'noop':
            instructions.append((True, int(d.split(" ")[1])))
        instructions.append((False, 0))
    return instructions


def part1(data):
    register = 1
    total = 0
    to_adds = defaultdict(lambda: 0)
    instructions = parse_data(data)

    for i in range(1, 221):
        instruction = instructions.pop(0)
        if instruction[0]:
            to_adds[i+1] = instruction[1]
        instructions.append(instruction)

        if i in [20, 60, 100, 140, 180, 220]:
            total += i * register

        register += to_adds[i]
        del to_adds[i]

    return total



def part2(data):
    register = 1
    to_adds = defaultdict(lambda: 0)
    instructions = parse_data(data)
    crt = []

    for i in range(0, 240):
        instruction = instructions.pop(0)
        if instruction[0]:
            to_adds[i+1] = instruction[1]
        instructions.append(instruction)

        if i > 0 and i % 40 == 0:
            crt += ['\n']
        crt.append('#' if abs(register - i % 40) < 2 else ' ')

        register += to_adds[i]

    return "".join(crt)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 13140
    assert part2(test_1.splitlines()) == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

