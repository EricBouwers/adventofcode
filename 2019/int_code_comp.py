from _operator import add, mul

OPERATORS = {
    1: lambda modes, mem, p, _: simple_ops(add, modes, mem, p),
    2: lambda modes, mem, p, _: simple_ops(mul, modes, mem, p),
    3: lambda modes, mem, p, args: set_val(modes, mem, p, args),
    4: lambda modes, mem, p, _: print_val(modes, mem, p),
    5: lambda modes, mem, p, _: jump_true(modes, mem, p),
    6: lambda modes, mem, p, _: jump_false(modes, mem, p),
    7: lambda modes, mem, p, _: simple_ops(less_than, modes, mem, p),
    8: lambda modes, mem, p, _: simple_ops(equals_to, modes, mem, p)
}


def less_than(x, y):
    return 1 if x < y else 0


def equals_to(x, y):
    return 1 if x == y else 0


def set_val(_, mem, p, args):
    mem[mem[p+1]] = args.pop(0)
    p += 2
    return mem, p


def print_val(modes, mem, p):
    val = _get_mem_val(modes, mem, p, 0)
    # print(val)
    p += 2
    return mem, p, val


def simple_ops(op, modes, mem, p):
    val_1 = _get_mem_val(modes, mem, p, 0)
    val_2 = _get_mem_val(modes, mem, p, 1)
    mem[mem[p + 3]] = op(val_1, val_2)
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


def _get_mem_val(modes, mem, p, i):
    if len(modes) > i and modes[i] == 1:
        return mem[p + 1 + i]
    else:
        return mem[mem[p + 1 + i]]


def intcode_comp(memory, args, get_output=False, pointer=0):
    max_p = len(memory)
    while pointer < max_p:
        cur_val = memory[pointer]
        op_and_modes = parse_op_and_modes(cur_val)

        if op_and_modes[0] == 99:
            return memory if not get_output else memory, pointer, None

        op = OPERATORS[op_and_modes[0]]
        output = op(op_and_modes[1:], memory, pointer, args)

        if len(output) == 3 and get_output:
            return output

        memory, pointer = output[0], output[1]
