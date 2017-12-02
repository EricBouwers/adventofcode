#!/usr/bin/python

import sys
import md5
from itertools import permutations, tee, izip

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

i = sys.argv[1].split("\n")
chars = 2 + 4
rooms = map(list,i)
start_pos = None
positions = []

for idxr, r in enumerate(rooms):
    for idxc, c in enumerate(r):
        if rooms[idxr][idxc] in "012345678":
           positions.append((int(rooms[idxr][idxc]),(idxr, idxc)))
        if rooms[idxr][idxc] == "0":
            start_pos = None

positions.sort(key=lambda x:x[0])
positions = map(lambda x:x[1], positions)
print positions 

for p in positions:
    print rooms[p[0]][p[1]]

def get_possible_steps(path, cur_pos):
    new_pos = [
        [cur_pos[0]-1, cur_pos[1]],
        [cur_pos[0]+1, cur_pos[1]],
        [cur_pos[0], cur_pos[1]-1],
        [cur_pos[0], cur_pos[1]+1]
    ]
    

    allowed_pos = []

    for idx, pos in enumerate(new_pos):
        c = rooms[pos[0]][pos[1]]  
        if c != "#":
            allowed_pos.append((path+c, (pos[0], pos[1])))
    
    return allowed_pos 

def print_state(state):
    return str(state[1][0]) + "_" +str(state[1][1])

def get_next_state(states):
    if len(states) > 0:
        current_state = states.pop(0)
    else:
        return None


num_pos = len(positions)
distances = [[None for j in xrange(num_pos)] for i in xrange(num_pos)]
for idx in range(num_pos):
    for idy in range(idx+1, num_pos):
        x = positions[idx]
        y = positions[idy]
        states = [("", x)]
        seen_states = dict()
        found = False
 
        while len(states) > 0 and not found:

            cur_pos = states.pop(0)
            key = print_state(cur_pos)
            while key in seen_states:
                cur_pos = states.pop(0)
                key = print_state(cur_pos)
            
            seen_states[key] = 0

            if not cur_pos:
                found = True
                print "no distance found", idx, idy
            else:
                 if cur_pos[1][0] == y[0] and cur_pos[1][1] == y[1]:
                     print "found one", idx, idy
                     found = True 
                     distances[idx][idy] = len(cur_pos[0])
                     distances[idy][idx] = len(cur_pos[0])
                 else:
                     states += get_possible_steps(*cur_pos)

best = 999*999
for p in permutations(range(num_pos)):
    if p[0] == 0:
        pairs = pairwise(p)
        dist = sum(map(lambda x: distances[x[0]][x[1]], pairwise(p)))
        best = min(best, dist)
print best        

best = 999*999
for p in permutations(range(num_pos)):
    if p[0] == 0:
        p = list(p)
        p.append(0)
        pairs = pairwise(p)
        dist = sum(map(lambda x: distances[x[0]][x[1]], pairwise(p)))
        best = min(best, dist)
print best        
