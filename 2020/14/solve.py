#!/usr/bin/env python
from itertools import permutations

test_1 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
test_2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
test_3 = """"""
test_4 = """"""


def part1(data):
    mask = None
    register = {}
    for line in data:
        if line.startswith("mask = "):
            mask = line[7:]
        else:
            parts = line.split(" = ")
            register_index = parts[0][4:-1]
            to_write = format(int(parts[1]), 'b').zfill(36)
            new_num = "".join([i[1] if i[0] == 'X' else i[0] for i in zip(mask, to_write)])
            register[register_index] = int(new_num, 2)
    return sum(register.values())


def part2(data):
    mask = None
    register = {}
    for i, line in enumerate(data):
        if line.startswith("mask = "):
            mask = line[7:]
        else:
            parts = line.split(" = ")
            to_write = int(parts[1])
            register_mask = format(int(parts[0][4:-1]), 'b').zfill(36)
            register_mask = "".join([
                i[1] if i[0] == '0' else '1' if i[0] == '1' else 'X' for i in zip(mask, register_mask)
            ])
            floating_bits = sum([x == 'X' for x in register_mask])
            for replacement in range(2**floating_bits):
                replacement = list(format(replacement, 'b').zfill(floating_bits))
                register_index = ''.join([str(replacement.pop(0)) if c == 'X' else c for c in register_mask])
                register[register_index] = to_write
    return sum(register.values())


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 165
    assert part2(test_2.splitlines()) == 208

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

