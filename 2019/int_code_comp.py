from _operator import add, mul
from collections import defaultdict

OPERATORS = {
    1: lambda modes, mem, p, _: simple_ops(add, modes, mem, p),
    2: lambda modes, mem, p, _: simple_ops(mul, modes, mem, p),
    3: lambda modes, mem, p, args: set_val(modes, mem, p, args),
    4: lambda modes, mem, p, _: print_val(modes, mem, p),
    5: lambda modes, mem, p, _: jump_true(modes, mem, p),
    6: lambda modes, mem, p, _: jump_false(modes, mem, p),
    7: lambda modes, mem, p, _: simple_ops(less_than, modes, mem, p),
    8: lambda modes, mem, p, _: simple_ops(equals_to, modes, mem, p),
    9: lambda modes, mem, p, _: adjust_relative(modes, mem, p)
}


def less_than(x, y):
    return 1 if x < y else 0


def equals_to(x, y):
    return 1 if x == y else 0


def set_val(mode_and_pointer, mem, p, args):

    write_to = mem[p + 1]
    if len(mode_and_pointer[1]) == 1 and mode_and_pointer[1][0] == 2:
        write_to += mode_and_pointer[0]

    mem[write_to] = args.pop(0)
    p += 2
    return mem, p


def print_val(modes, mem, p):
    val = _get_mem_val(modes, mem, p, 0)
    # print(val)
    p += 2
    return mem, p, val


def adjust_relative(modes, mem, p):
    val = _get_mem_val(modes, mem, p, 0)
    p += 2
    return mem, p, modes[0] + val


def simple_ops(op, modes_and_relative, mem, p):
    val_1 = _get_mem_val(modes_and_relative, mem, p, 0)
    val_2 = _get_mem_val(modes_and_relative, mem, p, 1)

    write_to = mem[p + 3]
    if len(modes_and_relative[1]) == 3 and modes_and_relative[1][2] == 2:
        write_to += modes_and_relative[0]

    mem[write_to] = op(val_1, val_2)
    p += 4
    return mem, p


def jump_true(modes, mem, p):
    val1 = _get_mem_val(modes, mem, p, 0)
    val2 = _get_mem_val(modes, mem, p, 1)
    if val1 != 0:
        return mem, val2
    else:
        p += 3
        return mem, p


def jump_false(modes, mem, p):
    val1 = _get_mem_val(modes, mem, p, 0)
    val2 = _get_mem_val(modes, mem, p, 1)
    if val1 == 0:
        return mem, val2
    else:
        p += 3
        return mem, p


def parse_op_and_modes(cur_val):
    parsed = []
    cur_val, op = divmod(cur_val, 100)
    parsed.append(op)

    while cur_val:
        cur_val, mode = divmod(cur_val, 10)
        parsed.append(mode)

    return parsed


def _get_mem_val(mode_and_position, mem, p, i):
    relative_base = mode_and_position[0]
    modes = mode_and_position[1]
    if len(modes) > i and modes[i] == 1:
        return mem[p + 1 + i]
    elif len(modes) > i and modes[i] == 2:
        return mem[relative_base + mem[p + 1 + i]]
    else:
        return mem[mem[p + 1 + i]]


def intcode_comp(memory, args, get_output=False, pointer=0, relative_pointer=0):

    if not isinstance(memory, defaultdict):
        new_memory = defaultdict(lambda: 0)
        for i in range(len(memory)):
            new_memory[i] = memory[i]
        memory = new_memory

    while True:
        cur_val = memory[pointer]
        op_and_modes = parse_op_and_modes(cur_val)

        if op_and_modes[0] == 99:
            return memory if not get_output else memory, pointer, None, relative_pointer

        op = OPERATORS[op_and_modes[0]]
        output = op([relative_pointer, op_and_modes[1:]], memory, pointer, args)

        if len(output) == 3 and op_and_modes[0] == 9:
            relative_pointer = output[2]
        elif len(output) == 3 and op_and_modes[0] == 4 and get_output:
            return output[0], output[1], output[2], relative_pointer

        memory, pointer = output[0], output[1]
