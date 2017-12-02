#!/usr/bin/python

import sys
from collections import defaultdict

instructions = sys.argv[1].split('\n')

program = []

registers = {'a':0, 'b':0, 'c':0, 'd':0}

for instruction in instructions:
    program.append(instruction)

program_length = len(program)

def run_program():
    index = 0    
    out = []
    while index < len(program) and len(out) < 20:
        instruction = program[index]
        parts = instruction.split()
 
        if instruction.startswith("cpy"):
            index += 1         
            if parts[1] in 'abcd':
                registers[parts[2]] = registers[parts[1]]
            else:    
                registers[parts[2]] = int(parts[1])
        elif instruction.startswith("dec"):
            registers[parts[1]] -= 1
            index += 1         
        elif instruction.startswith("inc"):
            registers[parts[1]] += 1
            index += 1         
        elif instruction.startswith("tgl"):
            x = registers[parts[1]] if parts[1] in 'abcd' else int(parts[1])
            x = x+index
            if x < program_length-1:
                 x_parts = program[x].split()
                 if len(x_parts) == 2:
                     if program[x].startswith("inc"):
                         program[x] = program[x].replace("inc", "dec")
                     else:
                         program[x] = " ".join(["inc", x_parts[1]])
                 else:
                     if program[x].startswith("jnz"):
                         program[x] = program[x].replace("jnz", "cpy")
                     else:
                         program[x] = " ".join(["jnz", x_parts[1], x_parts[2]])
            index += 1             
        elif instruction.startswith("out"):
            x = registers[parts[1]] if parts[1] in 'abcd' else int(parts[1])
            out.append(str(x)) 
            index += 1
        else:
            x = registers[parts[1]] if parts[1] in 'abcd' else int(parts[1])
            y = registers[parts[2]] if parts[2] in 'abcd' else int(parts[2])
            if x > 0:
                index += y 
            else:
                index += 1
        
    return out        

goal1 = "0-1-"*8
goal2 = "1-0-"*8
for i in range(500000):
    registers["a"] = i 
    registers["b"] = 0 
    registers["c"] = 0 
    registers["d"] = 0 
    sequence = "-".join(run_program())

    print i, sequence
    if sequence.startswith(goal1) or sequence.startswith(goal2):
        exit()

        

        
