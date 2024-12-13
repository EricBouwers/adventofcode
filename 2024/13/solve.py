#!/usr/bin/env python
import re

test_1 = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
test_2 = """"""


def parse_data(data):
    machines = []
    for i in range(0, len(data), 4):
        a = complex(*[int(x) for x in re.findall('[0-9]+', data[i])])
        b = complex(*[int(x) for x in re.findall('[0-9]+', data[i+1])])
        p = complex(*[int(x) for x in re.findall('[0-9]+', data[i+2])])
        machines.append((a, b, p))
    return machines


def get_pushes(a, b, p):
    denom = a.real * b.imag - b.real * a.imag
    if denom == 0:
        return None, None
    else:
        A = (p.real * b.imag - b.real * p.imag) / denom
        B = (a.real * p.imag - p.real * a.imag) / denom
        return (A, B) if A.is_integer() and B.is_integer() else (None, None)


def part1(data):
    parsed = parse_data(data)

    tokens = 0
    for machine in parsed:
        a_count, b_count = get_pushes(*machine)
        if a_count is not None and a_count < 101 and b_count is not None and b_count < 101:
            tokens += (3 * a_count) + b_count

    return tokens


def part2(data):
    parsed = parse_data(data)

    tokens = 0
    for machine in parsed:
        a_count, b_count = get_pushes(machine[0], machine[1], machine[2] + 10000000000000+10000000000000j)
        if a_count is not None and b_count is not None:
            tokens += (3 * a_count) + b_count

    return tokens


if __name__ == '__main__':

    # assert part1(test_1.splitlines()) == 480
    assert part2(test_1.splitlines()) > 0


    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

