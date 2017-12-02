#!/usr/bin/python

import sys
import md5
from copy import deepcopy

rooms = [
 ["#","#","#","#","#","#","#","#","#"],
 ["#"," ","|"," ","|"," ","|"," ","#"],
 ["#","-","#","-","#","-","#","-","#"],
 ["#"," ","|"," ","|"," ","|"," ","#"],
 ["#","-","#","-","#","-","#","-","#"],
 ["#"," ","|"," ","|"," ","|"," ","#"],
 ["#","-","#","-","#","-","#","-","#"],
 ["#"," ","|"," ","|"," ","|"," "," "],
 ["#","#","#","#","#","#","#"," ","#"],
]

start_path = "bwnlcvfs"
start_pos = (1,1)
x_des = 7
y_des = 7
find_longest = True

def get_possible_steps(path, cur_pos):
    new_pos = [
        # step_X, step_y, direction, new_pos_x, new_pos_y    
        [cur_pos[0]-1, cur_pos[1], "U", cur_pos[0]-2, cur_pos[1]],
        [cur_pos[0]+1, cur_pos[1], "D", cur_pos[0]+2, cur_pos[1]],
        [cur_pos[0], cur_pos[1]-1, "L", cur_pos[0], cur_pos[1]-2],
        [cur_pos[0], cur_pos[1]+1, "R", cur_pos[0], cur_pos[1]+2],
    ]

    allowed_pos = []

    h = md5.new(path).hexdigest()
    for idx, pos in enumerate(new_pos):
        c = rooms[pos[0]][pos[1]]  
        if (c in "-|" and h[idx] in "bcdef") or c == " ":
            allowed_pos.append((path + pos[2], (pos[3], pos[4])))

    return filter(lambda x: valid_pos(*x[1]), allowed_pos)

def valid_pos(x, y):
    if x < 0 or y < 0:
        return False

    if x > 7 or y > 7:
        return False

    return True

def print_state(state):
    return state[0] + str(state[1][0]) + str(state[1][1]) 

states = [(start_path, start_pos)]
seen_states = set()
longest = 0

while len(states) > 0:
    current_state = states.pop(0)

    while print_state(current_state) in seen_states and states:
        current_state = states.pop(0)
    seen_states.add(print_state(current_state))

    cur_pos = current_state[1]
    if cur_pos[0] == x_des and cur_pos[1] == y_des: 
        print current_state
        if find_longest:
           current_length = len(current_state[0])
           longest = current_length if current_length > longest else longest
    else:
        states += get_possible_steps(*current_state)

print longest - len(start_path)       
