#!/usr/bin/env python

import sys
from collections import defaultdict

example1 = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""


example2 = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""


def get_val(val, regs):
    try:
        return int(val)
    except:
        return regs[val]


def process_one(x):
    registers = defaultdict(lambda:0)
    last_played = -1
    index = 0
    instructions = x.split("\n")
    
    while 0 <= index < len(instructions):
        parts = instructions[index].split(" ")

        if parts[0] == "snd":
            last_played = registers[parts[1]]
        elif parts[0] == "set":
            registers[parts[1]] = get_val(parts[2], registers)
        elif parts[0] == "add":
            registers[parts[1]] += get_val(parts[2], registers)
        elif parts[0] == "mul":
            registers[parts[1]] *= get_val(parts[2], registers)
        elif parts[0] == "mod":
            registers[parts[1]] %= get_val(parts[2], registers)
        elif parts[0] == "rcv":
            if last_played > 0:
                return last_played
        elif parts[0] == "jgz":
            if get_val(parts[1], registers) > 0:
                index += int(parts[2])
            else:
                index += 1
              
        if parts[0] != "jgz":
            index += 1


def process_two(x):
    registers0, registers1 = defaultdict(lambda:0), defaultdict(lambda:0)
    registers1['p'] = 1
    
    messages0, messages1 = [], []
    index0, index1 = 0, 0
    instructions = x.split("\n")
    
    thread0Wait, thread1Wait = False, False

    index = index0
    send_messages = messages1
    rec_messages = messages0
    registers = registers0
    curThread = 0
    thread1sent = 0

    while not all([thread0Wait, thread1Wait]):
        parts = instructions[index].split(" ")

        if parts[0] == "snd":
             send_messages.append(get_val(parts[1], registers))
             if curThread == 0:
                thread1Wait = False 
             else:
                thread0Wait = False
                thread1sent += 1
        elif parts[0] == "set":
            registers[parts[1]] = get_val(parts[2], registers)
        elif parts[0] == "add":
            registers[parts[1]] += get_val(parts[2], registers)
        elif parts[0] == "mul":
            registers[parts[1]] *= get_val(parts[2], registers)
        elif parts[0] == "mod":
            registers[parts[1]] %= get_val(parts[2], registers)
        elif parts[0] == "rcv":
            if len(rec_messages) > 0:
                registers[parts[1]] = rec_messages.pop(0)
            else:
                if curThread == 0:
                    thread0Wait = True
                    index0, index = index, index1-1 # -1 here, will be incremented below
                    send_messages, rec_messages = messages0, messages1
                    registers = registers1
                    curThread = 1
                else:                
                    thread1Wait = True
                    index1, index = index, index0-1 # -1 here, will be incremented below
                    send_messages, rec_messages = messages1, messages0
                    registers = registers0
                    curThread = 0

        elif parts[0] == "jgz":
            if get_val(parts[1], registers) > 0:
                index += get_val(parts[2], registers)
            else:
                index += 1
              
        if parts[0] != "jgz":
            index += 1

    return thread1sent


if __name__ == '__main__':
    
    assert process_one(example1) == 4
    print process_one(sys.argv[1])

    assert process_two(example2) == 3
    print process_two(sys.argv[1])

