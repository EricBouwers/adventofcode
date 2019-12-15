#!/usr/bin/env python

import sys

from int_code_comp import intcode_comp

test_1 = """"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


DIRECTION_TO_STEPS = {
    1: (0, 1),  # N
    4: (1, 0),  # E
    2: (0, -1),  # S
    3: (-1, 0),  # W
}


def take_step(pos, d):
    return (pos[0] + DIRECTION_TO_STEPS[d][0],
            pos[1] + DIRECTION_TO_STEPS[d][1])


def part1(data):
    start_memory = [int(x) for x in data.split(",")]
    cur_memory = [x for x in start_memory]
    pointer = 0
    relative_pointer = 0

    world = {(0, 0): "D"}

    cur_pos = (0, 0)
    steps = [(cur_pos, 0, d) for d in DIRECTION_TO_STEPS]

    pos_states = {cur_pos: (cur_memory.copy(), pointer, relative_pointer)}
    seen_pos = set()

    while len(steps) > 0:
        cur_pos, steps_taken, step_to_take = steps.pop()
        new_pos = take_step(cur_pos, step_to_take)
        seen_pos.add(new_pos)

        cur_memory, pointer, relative_pointer = pos_states[cur_pos]
        memory, pointer, s, relative_pointer = intcode_comp(cur_memory.copy(), [step_to_take], True, pointer, relative_pointer)

        if s == 0:
            world[new_pos] = "#"
        elif s == 1:
            world[new_pos] = "."
            pos_states[new_pos] = (memory, pointer, relative_pointer)
            steps = steps + [(new_pos, steps_taken + 1, d) for d in DIRECTION_TO_STEPS if take_step(new_pos, d) not in seen_pos]
        elif s == 2:
            world[new_pos] = "$"
            for y in range(-25, 25):
                line = ""
                for x in range(-25, 30):
                    line += world.get((x, y), " ")
                print(line)

            return steps_taken + 1


def part2(data):
    start_memory = [int(x) for x in data.split(",")]
    cur_memory = [x for x in start_memory]
    pointer = 0
    relative_pointer = 0

    world = {(0, 0): "."}

    cur_pos = (0, 0)
    steps = [(cur_pos, 0, d) for d in DIRECTION_TO_STEPS]

    pos_states = {cur_pos: (cur_memory.copy(), pointer, relative_pointer)}
    seen_pos = set()
    oxygen_positions = []

    while len(steps) > 0:
        cur_pos, steps_taken, step_to_take = steps.pop()
        new_pos = take_step(cur_pos, step_to_take)
        seen_pos.add(new_pos)

        cur_memory, pointer, relative_pointer = pos_states[cur_pos]
        memory, pointer, s, relative_pointer = intcode_comp(cur_memory.copy(), [step_to_take], True, pointer, relative_pointer)

        if s == 0:
            world[new_pos] = "#"
        else:
            if s == 2:
                oxygen_positions = [new_pos]

            world[new_pos] = "." if s == 1 else "O"
            pos_states[new_pos] = (memory, pointer, relative_pointer)
            steps = steps + [(new_pos, steps_taken + 1, d) for d in DIRECTION_TO_STEPS if take_step(new_pos, d) not in seen_pos]

    for y in range(-25, 25):
        line = ""
        for x in range(-25, 30):
            line += world.get((x, y), " ")
        print(line)

    open_locations = sum([1 for x in world.values() if x == "."])
    seconds = 0

    while open_locations > 0:
        seconds += 1

        for x in oxygen_positions:
            for d in DIRECTION_TO_STEPS:
                new_pos = take_step(x, d)
                if world[new_pos] == ".":
                    world[new_pos] = "O"

        oxygen_positions = []
        open_locations = 0
        for k, v in world.items():
            if v == ".":
                open_locations += 1
            elif v == "O":
                oxygen_positions.append(k)

    return seconds

if __name__ == '__main__':

    with open('input') as f:
        data = f.read()

    print(part1(data))
    print(part2(data))

