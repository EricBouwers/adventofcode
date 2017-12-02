#!/usr/bin/python

import sys
from copy import deepcopy

example = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""

input_1 = """The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
The third floor contains a thulium-compatible microchip.
The fourth floor contains nothing relevant."""

input_2 = """The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip, An elerium generator, An elerium-compatible microchip, A dilithium generator, A dilithium-compatible microchip.
The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
The third floor contains a thulium-compatible microchip.
The fourth floor contains nothing relevant."""

description = input_2.split('\n')

state = {0: [],1: [],2: [],3: []}

for idx, line in enumerate(description):
    if " a " in line:
        parts = line.split()
        for x in xrange(0, len(parts)):
            if "microchip" in parts[x]:
                state[idx].append(parts[x-1][0] + "M")
            if "generator" in parts[x]:
                state[idx].append(parts[x-1][0] + "G")

print state

def get_possible_states(distance, elevator, state):
    new_states = []
    floor_state = state[elevator]
    possible_single_combinations = [[i] for i in floor_state]
    possible_double_combinations = []

    for idx, i in enumerate(floor_state):
        for x in xrange(idx+1, len(floor_state)):
                possible_double_combinations.append([i, floor_state[x]])

    if elevator < 3:
        if possible_double_combinations:
            for c in possible_double_combinations:
                new_states.append(apply_move((1, c),[distance, elevator, deepcopy(state)]))
       
        new_states = filter(valid_state, new_states)                    
        if not new_states:
            for c in possible_single_combinations:
                new_states.append(apply_move((1, c),[distance, elevator, deepcopy(state)]))

    new_states = filter(valid_state, new_states)
    count = len(new_states)                    
    if elevator > 0:
        for c in possible_single_combinations:
            new_states.append(apply_move((-1, c),[distance, elevator, deepcopy(state)]))

        new_states = filter(valid_state, new_states)                    
        if len(new_states) == count:
            for c in possible_double_combinations:
                new_states.append(apply_move((-1, c),[distance, elevator, deepcopy(state)]))

    return filter(valid_state, new_states)    

def valid_state(state):
    floors = state[2]

    return all(map(valid_floor, floors.values())) 

def valid_floor(floor):
    chips = [i for i in floor if i[1] == "M"]
    gens = [i for i in floor if i[1] == "G"]

    if len(gens) > 0:
        for c in chips:
            if c[0] + "G" not in gens:
                return False

    return True

def apply_move(move, current_pos):
    old_level = current_pos[1]
    current_pos[0] += 1
    current_pos[1] += move[0]

    for i in move[1]:
        current_pos[2][old_level].remove(i)
        current_pos[2][current_pos[1]].append(i)

    return current_pos

def print_state(state):
    result = str(state[1])

    for f, items in state[2].items():
        for i in sorted(items):
            result += str(f) + str(i)
   
    return result

current_state = [0, 0, state]
states = [current_state]

seen_states = set()

while len(states) > 0:
    current_state = states.pop(0)

    while print_state(current_state) in seen_states and states:
        current_state = states.pop(0)
    seen_states.add(print_state(current_state))
    

    floors = current_state[2]
    if len(floors[0]) == 0 and len(floors[1]) == 0 and len(floors[2]) == 0:
        print current_state
        print current_state[0]
        exit()
    else:
        states += get_possible_states(*current_state)

    print current_state[0], current_state



