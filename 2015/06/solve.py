#!/usr/bin/env python
from collections import defaultdict

test_1 = """turn on 0,0 through 999,999"""
test_2 = """turn on 0,0 through 0,0"""

STEP_1_FUNCTIONS = {
  'turnon': lambda _: True,
  'turnoff': lambda _: False,
  'toggle': lambda x: not x,
}

STEP_2_FUNCTIONS = {
  'turnon': lambda x: x + 1,
  'turnoff': lambda x: max(0, x - 1),
  'toggle': lambda x: x + 2,
}

def parse_data(data, functions):
    steps = []

    for line in data:
        line = line.replace('turn on ', 'turnon;').replace('turn off ', 'turnoff;').replace('toggle ', 'toggle;').replace(' through ', ';')
        parts = line.split(';')
        steps.append([
            functions[parts[0]],
            [int(x) for x in parts[1].split(',')],
            [int(x) for x in parts[2].split(',')]
        ])

    return steps


def run_steps(steps, grid):
    for step in steps:
        func = step[0]
        x1, y1 = step[1]
        x2, y2 = step[2]
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid[(y, x)] = func(grid[(y, x)])

    return grid

def part1(data):
    steps = parse_data(data, STEP_1_FUNCTIONS)
    grid = defaultdict(lambda: False)

    return sum(run_steps(steps, grid).values())


def part2(data):
    steps = parse_data(data, STEP_2_FUNCTIONS)
    grid = defaultdict(lambda: 0)

    return sum(run_steps(steps, grid).values())


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 1000000
    assert part2(test_2.splitlines()) == 1

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

