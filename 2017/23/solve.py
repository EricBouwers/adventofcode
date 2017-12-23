#!/usr/bin/env python

import sys
from collections import defaultdict

def get_val(val, regs):
    try:
        return int(val)
    except:
        return regs[val]


def process_one(x):
    registers = defaultdict(lambda:0)
    index = 0
    instructions = x.split("\n")
    muls = 0
    
    while 0 <= index < len(instructions):
        parts = instructions[index].split(" ")
        
        if parts[0] == "set":
            registers[parts[1]] = get_val(parts[2], registers)
        elif parts[0] == "sub":
            registers[parts[1]] -= get_val(parts[2], registers)
        elif parts[0] == "mul":
            registers[parts[1]] *= get_val(parts[2], registers)
            muls += 1
        elif parts[0] == "jnz":
            if get_val(parts[1], registers) != 0:
                index += int(parts[2]) - 1
              
        index += 1

    return muls, registers["h"]


def is_prime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True


def process_2():
    b = 67
    b *= 100
    b -= -100000
    h = 0
  
    for i in xrange(0, 1001):
        h += 0 if is_prime(b+(17*i)) else 1

    return h


if __name__ == '__main__':
    
    print process_one(sys.argv[1])
    print process_2()
