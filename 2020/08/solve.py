#!/usr/bin/env python

test_1 = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

operators = {
    'nop': lambda arg, idx, acc: (idx+1, acc),
    'jmp': lambda arg, idx, acc: ((idx+arg), acc),
    'acc': lambda arg, idx, acc: ((idx+1), (acc+arg)),
}


def parse_statement(stm):
    parts = stm.split()
    return [parts[0], int(parts[1])]


def parse_program(data):
    return [parse_statement(i) for i in data]


def loop_until_end(program):
    acc = 0
    idx = 0
    seen_idx = set()
    max_idx = len(program)
    while idx not in seen_idx and idx < max_idx:
        seen_idx.add(idx)
        idx, acc = operators[program[idx][0]](program[idx][1], idx, acc)

    return acc, idx in seen_idx


def part1(data):
    program = parse_program(data)
    return loop_until_end(program)[0]


def part2(data):
    orig_program = parse_program(data)
    copy_program = [s for s in orig_program]
    for idx, stm in enumerate(orig_program):
        if stm[0] == 'acc':
            continue

        if stm[0] == 'jmp':
            copy_program[idx][0] = 'nop'
            old_stm = 'jmp'
        elif stm[0] == 'nop':
            copy_program[idx][0] = 'jmp'
            old_stm = 'nop'

        acc, loops = loop_until_end(copy_program)
        if not loops:
            return acc
        else:
            copy_program[idx][0] = old_stm


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 5
    assert part2(test_1.splitlines()) == 8

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

