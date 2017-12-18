#!/usr/bin/env python

import sys
from collections import defaultdict

example = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""


def process(x):
    registers = defaultdict(lambda:0)
    last_played = -1
    index = 0
    instructions = x.split("\n")
    
    while index < len(instructions):
        parts = instructions[index].split(" ")

        if parts[0] == "snd":
            last_played = registers[parts[1]]
        elif parts[0] == "set":
            registers[parts[1]] = int(parts[2]) if parts[2].isdigit() or parts[2][0] == "-" else registers[parts[2]]
        elif parts[0] == "add":
            registers[parts[1]] += int(parts[2]) if parts[2].isdigit() or parts[2][0] == "-"  else registers[parts[2]]
        elif parts[0] == "mul":
            registers[parts[1]] *= int(parts[2]) if parts[2].isdigit() or parts[2][0] == "-" else registers[parts[2]]
        elif parts[0] == "mod":
            val = (int(parts[2]) if parts[2].isdigit() else registers[parts[2]])
            registers[parts[1]] = (registers[parts[1]] % val) if val > 0 else 0 
        elif parts[0] == "rcv":
            if last_played > 0:
                return last_played
        elif parts[0] == "jgz":
            if registers[parts[1]] > 0:
                index += int(parts[2])
            else:
                index += 1
              
        if parts[0] != "jgz":
            index += 1



if __name__ == '__main__':
    
    assert process(example) == 4
    print process(sys.argv[1])


