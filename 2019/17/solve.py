#!/usr/bin/env python

import sys

from int_code_comp import intcode_comp

test_1 = """"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data):
    world = parse_world(data)
    print_world(world)

    allignment = 0
    for k, v in world.items():
        if v == "#":
            if all([world.get((k[0], k[1]+1), "") == "#", world.get((k[0], k[1]-1), "") == "#",
                    world.get((k[0]+1, k[1]), "") == "#", world.get((k[0]-1, k[1]), "") == "#"]):
                allignment += k[0] * k[1]

    return allignment


def parse_world(data):
    memory = [int(x) for x in data.split(",")]
    pointer = 0
    relative_pointer = 0
    finished = False
    world = {}
    cur_pos = (0, 0)

    while not finished:
        memory, pointer, s, relative_pointer = intcode_comp(memory, [], True, pointer, relative_pointer)

        if s is None:
            finished = True
        else:
            if s != 10:
                world[cur_pos] = str(chr(s))

            if s == 10:
                cur_pos = (0, cur_pos[1] + 1)
            else:
                cur_pos = (cur_pos[0] + 1, cur_pos[1])

    return world


def print_world(world):
    for y in range(51):
        line = ""
        for x in range(45):
            line += world[(x, y)]
        print(line)


DIRECTION_TO_STEPS = {
    "^": [(0, -1), "<", ">"],
    "<": [(-1, 0), "v", "^"],
    "v": [(0, 1), ">", "<"],
    ">": [(1, 0), "^", "v"],
}


def take_step(cur_pos, step):
    return cur_pos[0] + step[0], cur_pos[1] + step[1]


def part2(data):
    world = parse_world(data)

    cur_pos = None
    for k, v in world.items():
        if v == "^":
            cur_pos = k

    path = []
    seens = set()
    cur_direction = "^"
    can_move = True

    while can_move:
        try_step = take_step(cur_pos, DIRECTION_TO_STEPS[cur_direction][0])

        if world.get(try_step, "") == "#":
            seens.add(cur_pos)
            path[-1] += 1
            cur_pos = try_step
        else:
            left, right = DIRECTION_TO_STEPS[cur_direction][1:]
            right_step = take_step(cur_pos, DIRECTION_TO_STEPS[right][0])
            left_step = take_step(cur_pos, DIRECTION_TO_STEPS[left][0])

            if right_step not in seens and world.get(right_step, "") == "#":
                cur_direction = right
                path.append("R")
                path.append(0)
            elif left_step not in seens and world.get(left_step, "") == "#":
                cur_direction = left
                path.append("L")
                path.append(0)
            else:
                can_move = False

    print(",".join(map(str, path)))

    main = "A,C,A,C,B,B,C,B,C,A\n"
    func_a = "R,12,L,8,R,12\n"
    func_b = "R,8,L,8,R,8,R,4,R,4\n"
    func_c = "R,8,R,6,R,6,R,8\n"
    interactive = "n\n"

    all_input = main + func_a + func_b + func_c + interactive
    args = [ord(c) for c in all_input]

    memory = [int(x) for x in data.split(",")]
    memory[0] = 2

    pointer = 0
    relative_pointer = 0
    finished = False
    world = {}
    cur_pos = (0, 0)
    output = None
    while not finished:
        memory, pointer, s, relative_pointer = intcode_comp(memory, args, True, pointer, relative_pointer)

        if s is None:
            finished = True
        elif s > 10000:
            output = s
        else:
            if s != 10:
                world[cur_pos] = str(chr(s))

            if s == 10:
                cur_pos = (0, cur_pos[1] + 1)
            else:
                cur_pos = (cur_pos[0] + 1, cur_pos[1])

    print_world(world)
    return output

if __name__ == '__main__':

    with open('input') as f:
        data = f.read()

    print(part1(data))
    print(part2(data))

