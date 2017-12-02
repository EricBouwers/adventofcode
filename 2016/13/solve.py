#!/usr/bin/python

import sys
from copy import deepcopy

fav_num = int(sys.argv[1])
x_des = int(sys.argv[2])
y_des = int(sys.argv[3])

start_pos = (1,1)

w = 100
h = 100
my_map= [["_" for x in range(w)] for y in range(h)]


def get_possible_steps(distance, cur_pos):
    new_pos = [
        (cur_pos[0], cur_pos[1]+1),
        (cur_pos[0]+1, cur_pos[1]),
        (cur_pos[0], cur_pos[1]-1),
        (cur_pos[0]-1, cur_pos[1]),
    ]

    return map(lambda x: (distance+1, x), filter(lambda x: valid_pos(*x), new_pos))

def valid_pos(x, y):
    if x < 0 or y < 0:
        return False

    if my_map[y][x] == "_":
        my_map[y][x] = get_value(x, y)

    return my_map[y][x] != "#"

def get_value(x, y):
    num = x*x + 3*x + 2*x*y + y + y*y
    num += fav_num

    return "." if len("{0:b}".format(num).replace("0", "")) % 2 == 0 else "#"

def print_state(state):
    return str(state[1][0]) + str(state[1][1]) 

states = [(0, start_pos)]
seen_states = set()

while len(states) > 0:
    current_state = states.pop(0)

    while print_state(current_state) in seen_states and states:
        current_state = states.pop(0)
    seen_states.add(print_state(current_state))

    cur_pos = current_state[1]

    if cur_pos[0] == x_des and cur_pos[1] == y_des: 
        print current_state
        states = []
    else:
        states += get_possible_steps(*current_state)

states = [(0, start_pos)]
seen_states = set()

while states[0][0] < 51:
    
    current_state = states.pop(0)
    while print_state(current_state) in seen_states and states:
        current_state = states.pop(0)
    seen_states.add(print_state(current_state))

    cur_pos = current_state[1]

    states += get_possible_steps(*current_state)

print len(seen_states)
