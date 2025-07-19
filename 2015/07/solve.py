#!/usr/bin/env python
from collections import defaultdict
from functools import cache

test_1 = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""
test_2 = """"""


def get_value(wires, wire, c=None):
    c = {} if c is None else c
    if wire not in c:
        c[wire] = (int(wire) if wire.isnumeric() else wires[wire](wires, c)) & 0xFFFF
    return c[wire]

def parse_func(desc:str):
    if desc.isnumeric():
        return lambda w, c: int(desc)
    elif 'NOT' in desc:
        return lambda wires, c: ~ get_value(wires, desc.split(' ')[1], c)
    elif 'AND' in desc:
        return lambda wires, c: get_value(wires, desc.split(' ')[0], c) & get_value(wires, desc.split(' ')[2], c)
    elif 'OR' in desc:
        return lambda wires, c: get_value(wires, desc.split(' ')[0], c) | get_value(wires, desc.split(' ')[2], c)
    elif 'LSHIFT' in desc:
        return lambda wires, c: get_value(wires, desc.split(' ')[0], c) << get_value(wires, desc.split(' ')[2], c)
    elif 'RSHIFT' in desc:
        return lambda wires, c: get_value(wires, desc.split(' ')[0], c) >> get_value(wires, desc.split(' ')[2], c)
    elif desc.isascii():
        return lambda wires, c: get_value(wires, desc, c)
    else:
        return lambda wires, c: print(desc)

def parse_data(data):
    wires = {}
    for line in data:
        parts = line.split(' -> ')
        wires[parts[1]] = parse_func(parts[0])
    return wires


def part1(data, wire):
    wires = parse_data(data)
    return get_value(wires, wire)


def part2(data, wire):
    wires = parse_data(data)

    a_value = get_value(wires, wire)
    wires['b'] = lambda w, c: a_value
    return get_value(wires, wire)


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 'd') == 72
    assert part1(test_1.splitlines(), 'e') == 507
    assert part1(test_1.splitlines(), 'f') == 492
    assert part1(test_1.splitlines(), 'g') == 114
    assert part1(test_1.splitlines(), 'h') == 65412
    assert part1(test_1.splitlines(), 'i') == 65079
    assert part1(test_1.splitlines(), 'x') == 123
    assert part1(test_1.splitlines(), 'y') == 456

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines(), 'a'))
    print(part2(data.splitlines(), 'a'))

