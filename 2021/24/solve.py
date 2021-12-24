#!/usr/bin/env python
from collections import defaultdict
from operator import mul, add, floordiv, mod

test_1 = """inp z
inp x
mul z 3
eql z x"""
test_2 = """inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2"""
test_3 = """"""
test_4 = """"""

OPERATORS = {
    'inp': lambda mem, a, inp: read_input(a, inp, mem),
    'add': lambda mem, a, _: simple_ops(add, a, mem),
    'mul': lambda mem, a, _: simple_ops(mul, a, mem),
    'div': lambda mem, a, _: simple_ops(floordiv, a, mem),
    'mod': lambda mem, a, _: simple_ops(mod, a, mem),
    'eql': lambda mem, a, _: zero_if_equal(a, mem)
}


def simple_ops(op, a, mem):
    try:
        b = int(a[1])
    except:
        b = mem[a[1]]

    mem[a[0]] = op(mem[a[0]], b)
    return mem


def zero_if_equal(a, mem):
    try:
        b = int(a[1])
    except:
        b = mem[a[1]]

    mem[a[0]] = 1 if mem[a[0]] == b else 0
    return mem


def read_input(a, inp, mem):
    mem[a[0]] = inp.pop(0)
    return mem


def run_comp(data, inp):
    mem = defaultdict(lambda:0)
    for ins in data:
        ins = ins.split(" ")
        mem = OPERATORS[ins[0]](mem, ins[1:], inp)
    return mem


def part1(data):
    start = [9, 4, 9, 9, 2, 9, 9, 4, 1, 9, 5, 9, 9, 8]
    mem = run_comp(data, inp=start)
    print(mem)

    # w6 = w5 + 7
    # w8 = w7 - 5
    # w9 = w4 - 8
    # w11 = w10 - 4
    # w12 = w3
    # w13 = w2 + 5
    # w14 = w1 - 1


def part2(data):
    start = [2, 1, 1, 9, 1, 8, 6, 1, 1, 5, 1, 1, 6, 1]
    mem = run_comp(data, inp=start)
    print(mem)


if __name__ == '__main__':

    assert run_comp(test_1.splitlines(), [2, 3])['z'] == 0
    assert run_comp(test_1.splitlines(), [1, 3])['z'] == 1
    assert dict(run_comp(test_2.splitlines(), [12])) == {'w': 1, 'z': 0, 'y': 0, 'x': 1}

    with open('input') as f:
        data = f.read()

    print(part1(data.splitlines()))
    print(part2(data.splitlines()))

