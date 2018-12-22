#!/usr/bin/env python

import sys, re

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
    executed = 0

    lowest, highest = (None, None)
    seen = set()
    seen_list = 0

    while 0 <= isp and isp < program_length:
        regs[isp_reg] = isp
        ins = program[isp]
        regs[int(ins[3])] = opcodes[ins[0]](int(ins[1]), int(ins[2]), regs)
        isp = regs[isp_reg]
        isp += 1
        executed += 1
        
        if isp == 25:
            regs[3] = regs[4] // 256

        if isp == 29:
            if lowest is None:
                lowest = regs[5]
            if regs[5] not in seen:
                seen.add(regs[5])
                highest = regs[5]
                seen_list += 1
            else:
                isp = 100
    
    return lowest, highest


if __name__ == '__main__':

    data = sys.argv[1]
    print part1(data,1)
