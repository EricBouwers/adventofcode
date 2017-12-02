#!/usr/bin/python

import sys, operator

steps = sys.argv[1].split(", ")
pos = [0,0]
orientation = 0 # N, E, S, W
visited = []
first_twice = None

for step in steps:
    orientation += 1 if step[0] == "R" else -1
    orientation %= 4

    idx = 1 if orientation in [0,2] else 0
    op = operator.add if orientation <= 1 else operator.sub 

    steps = int(step[1:])

    for i in range(0, steps):
        pos[idx] = op(pos[idx], 1)
    
        if "{}_{}".format(*pos) in visited and not first_twice:
            first_twice = list(pos)
        visited.append("{}_{}".format(*pos))   
    
    print pos, visited

print pos, " is ", sum(map(abs, pos)),  " away"
print first_twice, " is the first position visited twice, ", sum(map(abs,first_twice)), " blocks away"


