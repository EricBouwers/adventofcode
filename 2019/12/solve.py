#!/usr/bin/env python
import math
import re
from itertools import combinations

test_1 = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
test_2 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""
test_3 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""
test_4 = """"""


def part1(data, steps):
    positions, velocities = parse_data(data)

    for i in range(steps):
        take_step(positions, velocities)

    total_energy = 0
    for moon in positions.keys():
        total_energy += sum(map(abs, positions[moon])) * sum(map(abs, velocities[moon]))

    return total_energy


def parse_data(data):
    positions = {}
    velocities = {}
    moon_count = 0
    for line in data:
        pos = [int(x) for x in re.findall(r'-?\d+', line)]
        vel = [0, 0, 0]
        positions[moon_count] = pos
        velocities[moon_count] = vel
        moon_count += 1

    return positions, velocities


def take_step(positions, velocities, axes=[0, 1, 2]):
    for a, b in combinations(positions.keys(), 2):
        pos_a, pos_b = positions[a], positions[b]
        for i in axes:
            grav = 0 if pos_a[i] == pos_b[i] else -1 if pos_a[i] > pos_b[i] else 1
            velocities[a][i] += grav
            velocities[b][i] += -grav
    for moon in positions.keys():
        positions[moon] = [x for x in map(sum, zip(positions[moon], velocities[moon]))]


def states_key(positions, velocities):
    return str(positions) + str(velocities)


def _simulate_axis(positions, velocities, axis):
    steps = 0
    states = set()
    states.add(states_key(positions, velocities))
    not_repeated = True
    while not_repeated:
        take_step(positions, velocities, [axis])
        steps += 1
        state = states_key(positions, velocities)

        if state in states:
            not_repeated = False
        else:
            states.add(state)

    return steps


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def part2(data):
    positions, velocities = parse_data(data)

    x_steps = _simulate_axis(positions, velocities, 0)
    y_steps = _simulate_axis(positions, velocities, 1)
    z_steps = _simulate_axis(positions, velocities, 2)

    return lcm(x_steps, lcm(y_steps, z_steps))


if __name__ == '__main__':

    assert part1(test_1.splitlines(), 10) == 179
    assert part1(test_2.splitlines(), 100) == 1940
    assert part2(test_1.splitlines()) == 2772
    assert part2(test_3.splitlines()) == 4686774924

    print("Done testing")

    with open('input') as f:
        data = f.readlines()

    print(part1(data, 1000))
    print(part2(data))

