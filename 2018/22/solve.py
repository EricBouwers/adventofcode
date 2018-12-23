#!/usr/bin/env python

import sys, re, heapq

ROCK = "."
WET = "="
NARROW = "|"

TORCH = 0
GEAR = 1
NEITHER = 2

def part1(depth, tx, ty):

    icave = []
    tcave = []
    risk = 0
    for y in range(0, ty*8):
        irow = []
        icave.append(irow)
        trow = []
        tcave.append(trow)
        for x in range(0, tx*8):
            
            if (x,y) in [(0,0), (tx, ty)]:
                irow.append((0 + depth) % 20183)
            elif y == 0:
                irow.append((x*16807 + depth) % 20183)
            elif x == 0:
                irow.append((y*48271 + depth) % 20183)
            else:
                irow.append((irow[-1] * icave[-2][x] + depth) % 20183)
            
            if (x,y) in [(0,0), (tx, ty)]:
                trow.append(ROCK)
            else:
                t_mod = irow[-1] % 3    
                risk += t_mod if x <= tx and y <= ty else 0
                trow.append(ROCK if t_mod == 0 else WET if t_mod == 1 else NARROW)    

    return risk, tcave

def part2(depth, tx, ty):
    _, tcave = part1(depth, tx, ty)

    return find_shortest_path((0,0), (tx, ty), tcave, len(tcave[0]), len(tcave))

def find_shortest_path(cur_pos, target, area, w, h):
    states = [(0, cur_pos, TORCH)]
    seen_states = {}
    len_states = 1

    new_area = {}
    for y in range(0,len(area)):
        for x in range(0, len(area[y])):
            new_area[(x,y)] = area[y][x]

    area = new_area    

    while len(states) > 0 and cur_pos is not None:
        mins, cur_pos, equip = heapq.heappop(states)
        len_states -= 1

        if cur_pos == target:
            return mins 

        while cur_pos and seen_states.get((cur_pos, equip), mins + 1) < mins:
            if len_states > 0:
                mins, cur_pos, equip = heapq.heappop(states)
                len_states -= 1
            else:
                cur_pos = None
       
        if cur_pos:
            seen_states[(cur_pos, equip)] = mins

            for s in get_possible_steps(mins, cur_pos, equip, area, target):
                if s and seen_states.get((s[1], s[2]), s[0] + 1) > s[0]:
                    seen_states[(s[1], s[2])] = s[0]
                    heapq.heappush(states, s)
                    len_states += 1

    return seen_states[target] 

def get_possible_steps(mins, cur_pos, equip, area, target):
    pos = [(cur_pos[0] + 1, cur_pos[1]), 
           (cur_pos[0] - 1, cur_pos[1]), 
           (cur_pos[0]    , cur_pos[1] + 1), 
           (cur_pos[0]    , cur_pos[1] - 1)]

    result = map(lambda p: get_paths(mins, cur_pos, p, equip, area, target) if p in area else None, pos)
    return result

def get_paths(mins, cur_pos, new_pos, equip, area, target):

    key = (area[cur_pos], area[new_pos], equip)
    
    if key in transitions:
        new_state = transitions[key](mins, new_pos)
        if new_state[2] != TORCH and new_state[1] == target: 
            return (new_state[0]+7, new_state[1], TORCH)
        else:
            return new_state
    else:
        return None

transitions = {
        (ROCK, ROCK, TORCH):   lambda m, p: (m+1, p, TORCH),
        (ROCK, ROCK, GEAR):    lambda m, p: (m+1, p, GEAR),
        (ROCK, WET, TORCH):    lambda m, p: (m+8, p, GEAR),
        (ROCK, WET, GEAR):     lambda m, p: (m+1, p, GEAR),
        (ROCK, NARROW, TORCH): lambda m, p: (m+1, p, TORCH),
        (ROCK, NARROW, GEAR):  lambda m, p: (m+8, p, TORCH),
        
        (WET, WET, NEITHER):   lambda m, p: (m+1, p, NEITHER),
        (WET, WET, GEAR):      lambda m, p: (m+1, p, GEAR),
        (WET, ROCK, NEITHER):  lambda m, p: (m+8, p, GEAR),
        (WET, ROCK, GEAR):     lambda m, p: (m+1, p, GEAR),
        (WET, NARROW, NEITHER):lambda m, p: (m+1, p, NEITHER),
        (WET, NARROW, GEAR):   lambda m, p: (m+8, p, NEITHER),
        
        (NARROW, NARROW, NEITHER): lambda m, p: (m+1, p, NEITHER),
        (NARROW, NARROW, TORCH):   lambda m, p: (m+1, p, TORCH),
        (NARROW, WET, NEITHER):    lambda m, p: (m+1, p, NEITHER),
        (NARROW, WET, TORCH):      lambda m, p: (m+8, p, NEITHER),
        (NARROW, ROCK, NEITHER):   lambda m, p: (m+8, p, TORCH),
        (NARROW, ROCK, TORCH):     lambda m, p: (m+1, p, TORCH)
}

if __name__ == '__main__':

    assert part1(510, 10, 10)[0] == 114
    assert part2(510, 10, 10) == 45

    print part1(8103, 9, 758)[0]
    print part2(8103, 9, 758)

