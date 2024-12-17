#!/usr/bin/env python
from copy import copy, deepcopy

test_1 = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
test_2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""


def parse_data(data):
    register = {'A': 0, 'B': 0, 'C': 0}
    program = []
    for d in data:
        if 'Register' in d:
            reg = d[9]
            register[reg] = int(d.split(" ")[2])
        elif d:
            program = [int(x) for x in d[9:].split(',')]
    return register, program


def get_operand_combo(operand, register):
    if operand == 4:
        return register['A']
    if operand == 5:
        return register['B']
    if operand == 6:
        return register['C']
    else:
        return operand


def adv(operand, register):
    register['A'] = register['A'] // (2 ** get_operand_combo(operand, register))
    return [], lambda x: x + 2


def bxl(operand, register):
    register['B'] = register['B'] ^ operand
    return [], lambda x: x + 2


def bst(operand, register):
    register['B'] = get_operand_combo(operand, register) % 8
    return [], lambda x: x + 2


def jnz(operand, register):
    if register['A'] == 0:
        return [], lambda x: x + 2
    else:
        return [], lambda x: operand


def bxc(operand, register):
    return bxl(register['C'], register)


def out(operand, register):
    x, y = divmod(get_operand_combo(operand, register), 8)
    return [y], lambda x: x + 2


def bdv(operand, register):
    register['B'] = register['A'] // (2 ** get_operand_combo(operand, register))
    return [], lambda x: x + 2


def cdv(operand, register):
    register['C'] = register['A'] // (2 ** get_operand_combo(operand, register))
    return [], lambda x: x + 2


OPERATIONS = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}


def intcode_comp(register, program):

    register = deepcopy(register)
    pointer = 0
    max_pointer = len(program)
    output = []

    while pointer < max_pointer:
        opcode = program[pointer]
        operand = program[pointer + 1]

        ins_out, jmp = OPERATIONS[opcode](operand, register)
        output.extend(ins_out)
        pointer = jmp(pointer)

    return output


def part1(data):
    register, program = parse_data(data)
    output = intcode_comp(register, program)

    return ",".join(map(str, output))

# The program
# B = A % 8
# B = B ^ 7
# C = A // (2**B)
# A = A // 3
# B = B ^ C
# B = B ^ 7
# return B % 8


def part2(data):
    register, program = parse_data(data)
    to_find = ",".join(map(str, program))

    results = []
    to_try = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    seen = set()
    while to_try:
        x = to_try.pop(0)
        register['A'] = x
        output = intcode_comp(register, program)
        if output == program:
            results.append(x)
        elif to_find.endswith(",".join(map(str, output))):
            for x in [x * 8 + t for t in range(0, 8)]:
                if x not in seen:
                    to_try.append(x)
                    seen.add(x)

    return min(results)


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == '4,6,3,5,6,3,5,2,1,0'
    assert part2(test_2.splitlines()) == 117440

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))




