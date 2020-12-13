#!/usr/bin/env python
from math import gcd

test_1 = """939
7,13,x,x,59,x,31,19"""
test_2 = """1
67,7,x,59,61"""
test_3 = """1
1789,37,47,1889"""


def part1(data):
    departure = int(data[0])
    busses = [int(b) for b in data[1].split(',') if b is not 'x']
    min_bus = max(busses) * 10000
    min_wait = min_bus
    for b in busses:
        bus_departs = departure if departure % b == 0 else departure + (b - (departure % b))
        cur_wait = bus_departs - departure
        if cur_wait < min_wait:
            min_bus = b
            min_wait = cur_wait
    return min_bus * min_wait


def part2(data, start=0):
    constraints = [(i, int(b)) for i, b in enumerate(data[1].split(',')) if b is not 'x']
    len_constraints = len(constraints)
    step_size = constraints[0][1]
    cur_time = start + (step_size - (start % step_size))
    next_constraint_index = 1
    next_constraint = constraints[next_constraint_index]
    while next_constraint:
        if (cur_time + next_constraint[0]) % next_constraint[1] == 0:
            next_bus = next_constraint[1]
            step_size = int(step_size * next_bus / gcd(step_size, next_bus))
            next_constraint_index += 1
            next_constraint = constraints[next_constraint_index] if next_constraint_index < len_constraints else None

        if sum([(cur_time + j) % b == 0 for j, b in constraints]) == len_constraints:
            return cur_time

        cur_time += step_size


if __name__ == '__main__':
    assert part1(test_1.splitlines()) == 295
    assert part2(test_1.splitlines(), 1000000) == 1068781
    assert part2(test_2.splitlines(), 1000000) == 1261476
    assert part2(test_3.splitlines(), 100000000) == 1202161486

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines(), 100000000000000))

