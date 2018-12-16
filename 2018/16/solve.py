#!/usr/bin/env python

import sys, re

example_input_1 = """Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]"""

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

def part1(data, poss=False):

    possibilities = { x : set(opcodes.keys()) for x in range(0,16)}
    three_or_more = 0

    before = None
    ins = None
    after = None

    for l in data.split("\n"):
        if "Before" in l:
            before = [int(x) for x in re.findall("\d+", l)]
        elif before is not None and "After" not in l:
            ins = [int(x) for x in re.findall("\d+", l)]
        elif "After" in l:    
            after = [int(x) for x in re.findall("\d+", l)]

        if before is not None and ins is not None and after is not None:
            same = []
            for op in opcodes:
                regs = { i:x for i,x in enumerate(before) }
                regs[ins[3]] = opcodes[op](ins[1], ins[2], regs)

                if regs.values() == after:
                    same.append(op)
            
            if len(same) >= 3:
                three_or_more += 1
            
            possibilities[ins[0]] = possibilities[ins[0]].intersection(set(same))
            before, ins, after = (None, None, None)
   
    return possibilities if poss else three_or_more

def part2(data1, data2):
    possibilities = part1(data1, True)
    chosen = {x:"" for x in range(0,16)}

    while "" in chosen.values():
        for i, poss in possibilities.items():
            if len(poss) == 1:
                chosen[i] = poss.pop()
                for other in possibilities.values():
                    if len(other) > 1 and chosen[i] in other:
                        other.remove(chosen[i])
    
    regs = { x:0 for x in range(0,4)}
    
    for line in data2.split("\n"):
        ins = [int(x) for x in re.findall("\d+", line)]
        regs[ins[3]] = opcodes[chosen[ins[0]]](ins[1], ins[2], regs)

    return regs[0]

if __name__ == '__main__':

    assert part1(example_input_1) == 1
    assert part1(example_input_1 + "\n" + example_input_1) == 2

    data1 = sys.argv[1]
    data2 = sys.argv[2]

    print part1(data1)
    print part2(data1, data2)

