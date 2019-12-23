#!/usr/bin/env python

import sys
from collections import defaultdict

from int_code_comp import parse_op_and_modes, OPERATORS

test_1 = """"""
test_2 = """"""
test_3 = """"""
test_4 = """"""


def part1(data):
    comps = {}

    memory = [int(x) for x in data.split(",")]
    for c in range(50):
        new_memory = defaultdict(lambda: 0)
        for i in range(len(memory)):
            new_memory[i] = memory[i]
        comps[c] = (new_memory, [c], 0, 0)

    outputs = defaultdict(list)

    while True:
        for i in range(50):
            memory, args, pointer, relative_pointer = comps[i]

            cur_val = memory[pointer]
            op_and_modes = parse_op_and_modes(cur_val)

            if op_and_modes[0] == 99:
                return memory, pointer, None, relative_pointer

            op = OPERATORS[op_and_modes[0]]

            if op_and_modes[0] == 3 and len(args) == 0:
                args.append(-1)

            output = op([relative_pointer, op_and_modes[1:]], memory, pointer, args)

            if len(output) == 3 and op_and_modes[0] == 9:
                relative_pointer = output[2]
            elif len(output) == 3 and op_and_modes[0] == 4:
                outputs[i].append(output[2])

                if len(outputs[i]) == 3:
                    print(outputs[i])
                    send_to = outputs[i][0]

                    if send_to == 255:
                        return outputs[i][2]
                    else:
                        comp2_m, comp2_a, comp2_pointer, comp2_relative_pointer = comps[send_to]
                        comps[send_to] = (comp2_m, comp2_a + outputs[i][1:], comp2_pointer, comp2_relative_pointer)
                        outputs[i] = []

            comps[i] = (output[0], args, output[1], relative_pointer)


def part2(data):
    comps = {}

    memory = [int(x) for x in data.split(",")]
    for c in range(50):
        new_memory = defaultdict(lambda: 0)
        for i in range(len(memory)):
            new_memory[i] = memory[i]
        comps[c] = (new_memory, [c], 0, 0)

    outputs = defaultdict(list)
    nat = []

    prev_send_to_zero = None
    empty_receives = {c: 0 for c in range(50)}

    while True:
        is_idle = True
        c = 0
        while is_idle and c < 50:
            is_idle = is_idle and empty_receives[c] > 1
            c += 1

        c = 0
        while is_idle and c < 50:
            is_idle = is_idle and len(comps[c][1]) == 0
            c += 1

        if is_idle and len(nat) > 0:
            comp2_m, comp2_a, comp2_pointer, comp2_relative_pointer = comps[0]
            comps[0] = (comp2_m, comp2_a + nat, comp2_pointer, comp2_relative_pointer)

            if nat[1] == prev_send_to_zero:
                return nat[1]
            else:
                prev_send_to_zero = nat[1]

            nat = []

        for i in range(50):
            memory, args, pointer, relative_pointer = comps[i]

            cur_val = memory[pointer]
            op_and_modes = parse_op_and_modes(cur_val)

            if op_and_modes[0] == 99:
                return memory, pointer, None, relative_pointer

            op = OPERATORS[op_and_modes[0]]

            if op_and_modes[0] == 3 and len(args) == 0:
                args.append(-1)
                empty_receives[i] += 1
            else:
                empty_receives[i] += 0

            output = op([relative_pointer, op_and_modes[1:]], memory, pointer, args)

            if len(output) == 3 and op_and_modes[0] == 9:
                relative_pointer = output[2]
            elif len(output) == 3 and op_and_modes[0] == 4:
                outputs[i].append(output[2])

                if len(outputs[i]) == 3:
                    print(outputs[i])
                    send_to = outputs[i][0]

                    if send_to == 255:
                        nat = outputs[i][1:]
                    else:
                        comp2_m, comp2_a, comp2_pointer, comp2_relative_pointer = comps[send_to]
                        comps[send_to] = (comp2_m, comp2_a + outputs[i][1:], comp2_pointer, comp2_relative_pointer)

                    outputs[i] = []

            comps[i] = (output[0], args, output[1], relative_pointer)


if __name__ == '__main__':

    with open('input') as f:
        data = f.read()

    print(part1(data))
    print(part2(data))

