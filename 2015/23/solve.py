#!/usr/bin/env python

test_1 = """inc a
jio a, +2
tpl a
inc a
"""
test_2 = """"""


def get_func(line):
    if 'hlf' in line:
        reg = 0 if line[-1] == 'a' else 1
        return lambda r: ([r[0] / 2 if reg == 0 else r[0], r[1] / 2 if reg == 1 else r[1]], 1)
    elif 'tpl' in line:
        reg = 0 if line[-1] == 'a' else 1
        return lambda r: ([r[0] * 3 if reg == 0 else r[0], r[1] * 3 if reg == 1 else r[1]], 1)
    elif 'inc' in line:
        ap = 1 if line[-1] == 'a' else 0
        bp = 1 if line[-1] == 'b' else 0
        return lambda r: ([r[0]+ap, r[1]+bp], 1)
    elif 'jmp' in line:
        jmp = int(line[3:])
        return lambda r: (r, jmp)
    elif 'jie' in line:
        reg = 0 if line[4] == 'a' else 1
        offset = int(line[7:])
        return lambda regs: (regs, (offset if regs[reg] % 2 == 0 else 1))
    elif 'jio' in line:
        reg = 0 if line[4] == 'a' else 1
        offset = int(line[7:])
        return lambda regs: (regs, (offset if regs[reg] == 1 else 1))

def parse_data(data):
    return [get_func(d) for d in data]

def run_program(data, reg):
    program = parse_data(data)

    i = 0
    max_i = len(program)

    while i < max_i:
        reg, jmp = program[i](reg)
        i += jmp

    return reg

def part1(data):
    return run_program(data, [0, 0])

def part2(data):
    return run_program(data, [1, 0])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == [2,0]

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))


# too high 26623
# too low 0