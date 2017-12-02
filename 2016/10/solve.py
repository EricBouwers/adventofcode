#!/usr/bin/python

import sys
from collections import defaultdict

instructions = sys.argv[1].split('\n')

class Bot(object):

    def __init__(self,**kwargs):
        self.numbers = set()
        self.bot_low = None
        self.output_low = None
        self.bot_high = None
        self.output_high = None

bots = defaultdict(lambda: Bot()) 
outputs = defaultdict(list)

for instruction in instructions:
    if "value" in instruction:
        parts = instruction.split()
        bots[parts[-1]].numbers.add(int(parts[1]))
    elif "gives" in instruction:
        parts = instruction.split()
        if parts[5] == "bot":
            bots[parts[1]].bot_low = parts[6]
        else:
            bots[parts[1]].output_low = parts[6]
        
        if parts[-2] == "bot":
            bots[parts[1]].bot_high = parts[-1]
        else:
            bots[parts[1]].output_high = parts[-1]

compare_61_and_17 = None

while len([b for b in bots.values() if len(b.numbers) > 1]):
    for name, b in bots.items():
        if len(b.numbers) == 2:

            if 61 in b.numbers and 17 in b.numbers:
                compare_61_and_17 = name

            if b.bot_low:
                bots[b.bot_low].numbers.add(min(b.numbers)) 
            else:
                outputs[b.output_low].append(min(b.numbers))
            
            if b.bot_high:
                bots[b.bot_high].numbers.add(max(b.numbers)) 
            else:
                outputs[b.output_high].append(max(b.numbers))
            
            b.numbers = []

for k, b in bots.items():
    print k, b.numbers

print outputs

print compare_61_and_17
