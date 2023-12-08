#!/usr/bin/env python
import math
from collections import deque

test_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
test_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
test_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def parse_data(data):
    ins = [0 if c == 'L' else 1 for c in data[0]]
    steps = {}
    for state in data[2:]:
        splits = state.replace("(", "").replace(")", "").split(" = ")
        steps[splits[0]] = splits[1].split(", ")

    return deque(ins), steps


def part1(data):
    ins, steps = parse_data(data)

    cur_state = 'AAA'
    steps_taken = 0
    while cur_state != 'ZZZ':
        cur_state = steps[cur_state][ins[0]]
        steps_taken += 1
        ins.rotate(-1)

    return steps_taken


def part2(data):
    ins, steps = parse_data(data)

    cur_states = [state for state in steps.keys() if state[-1] == 'A']

    total_steps = 1
    for cur_state in cur_states:
        new_ins = deque([x for x in ins])
        step_state = cur_state
        steps_taken = 0
        while step_state[-1] != 'Z':
            step_state = steps[step_state][new_ins[0]]
            steps_taken += 1
            new_ins.rotate(-1)
        total_steps = math.lcm(total_steps, steps_taken)

    return total_steps


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 2
    assert part1(test_2.splitlines()) == 6
    assert part2(test_3.splitlines()) == 6

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
