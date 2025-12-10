#!/usr/bin/env python
import heapq

import numpy as np
from scipy.optimize import milp, linprog, LinearConstraint
from z3 import Real, Solver, Int

test_1 = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
test_2 = """"""


def parse_data(data):
    machines = []
    for d in data:
        for c in "[]{}()":
            d = d.replace(c,"")
        parts = d.split(" ")
        machine = (
            parts[0],
            [list(map(int, b.split(","))) for b in parts[1:-1]],
            list(map(int, parts[-1].split(",")))
        )
        machines.append(machine)

    return machines


def full_buttons(buttons, joltages):
    complete_buttons = []
    for i in range(0, len(joltages)):
        joltage_button = [0] * len(buttons)
        for j, b in enumerate(buttons):
            joltage_button[j] = 1 if i in b else 0
        complete_buttons.append(joltage_button)
    return complete_buttons

def press_buttons_joltages(machine):
    buttons = machine[1]
    joltages = machine[-1]

    c = np.array([1] * len(buttons))
    A = np.array(full_buttons(buttons, joltages))
    b_u = np.array(joltages)

    constraints = LinearConstraint(A, b_u, b_u)
    integrality = np.ones_like(c)
    res = milp(c=c, constraints=constraints, integrality=integrality)

    return int(sum(res.x))

def press_button_lights(state, button):
    state = [s for s in state]
    for b in button:
        state[b] = '#' if state[b] == '.' else "."
    return "".join(state)


def press_buttons_lights(machine):
    target_state = machine[0]
    buttons = machine[1]

    states = []
    seen_states = {"." * len(target_state):0}
    heapq.heapify(states)
    heapq.heappush(states, (0, "." * len(target_state)))

    while states:
        presses, state = heapq.heappop(states)
        presses += 1
        for b in buttons:
            new_state = press_button_lights(state, b)

            if new_state == target_state:
                return presses
            elif new_state not in seen_states or seen_states[new_state] > presses:
                seen_states[new_state] = presses
                heapq.heappush(states, (presses, new_state))


def part1(data):
    machines = parse_data(data)
    return sum([press_buttons_lights(machine) for machine in machines])


def part2(data):
    machines = parse_data(data)
    return sum([press_buttons_joltages(machine) for machine in machines])


if __name__ == '__main__':

    assert part1(test_1.splitlines()) == 7
    assert part2(test_1.splitlines()) == 33

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))
