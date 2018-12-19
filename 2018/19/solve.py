#!/usr/bin/env python

import sys, re

example_input_1 = """seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5"""

opcodes = {
    "addr" : lambda a, b, regs: regs[a] + regs[b],
    "addi" : lambda a, b, regs: regs[a] + b,
    "mulr" : lambda a, b, regs: regs[a] * regs[b],
    "muli" : lambda a, b, regs: regs[a] * b,
    "banr" : lambda a, b, regs: regs[a] & regs[b],
    "bani" : lambda a, b, regs: regs[a] & b,
    "borr" : lambda a, b, regs: regs[a] | regs[b],
    "bori" : lambda a, b, regs: regs[a] | b,
    "setr" : lambda a, b, regs: regs[a],
    "seti" : lambda a, b, regs: a,
    "gtir" : lambda a, b, regs: 1 if a > regs[b] else 0,
    "gtri" : lambda a, b, regs: 1 if regs[a] > b else 0,
    "gtrr" : lambda a, b, regs: 1 if regs[a] > regs[b] else 0,
    "eqir" : lambda a, b, regs: 1 if a == regs[b] else 0,
    "eqri" : lambda a, b, regs: 1 if regs[a] == b else 0,
    "eqrr" : lambda a, b, regs: 1 if regs[a] == regs[b] else 0
}

def part1(data, isp_reg, reg_0=0):

    regs = {i:0 for i in range(0,6)}
    regs[0] = reg_0

    program = [line.split(" ") for line in data.split("\n")]
    program_length = len(program)
    isp = 0
    
    while 0 <= isp and isp < program_length:
        regs[isp_reg] = isp
        ins = program[isp]
        regs[int(ins[3])] = opcodes[ins[0]](int(ins[1]), int(ins[2]), regs)
        isp = regs[isp_reg]
        isp += 1

    return regs[0]

def part2(upto):
    return sum([x for x in range(1,upto) if upto % x == 0]) + upto

if __name__ == '__main__':

    assert part1(example_input_1,0) == 6

    data = sys.argv[1]

    print part1(data,3)
    print part2(926)
    print part2(10551326) # number in reg[4] after some iterations in part 1

