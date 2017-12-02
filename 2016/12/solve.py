#!/usr/bin/python

import sys
from collections import defaultdict

instructions = sys.argv[1].split('\n')

program = []
registers = {'a':0, 'b':0, 'c':1, 'd':0}

for instruction in instructions:
    program.append(instruction)

index = 0    
program_length = len(program)

while index < len(program):
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
    else:
        x = registers[parts[1]] if parts[1] in 'abcd' else int(parts[1])
        if x > 0:
            index += int(parts[2])
        else:
            index += 1

    print index

print registers            
            
        

        
