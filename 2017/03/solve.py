#!/usr/bin/env python

import sys
import itertools as it

right = 1
up = 2
left = 3
down = 4

def calc_grid(limit):
    grid = {(0,0):1, (0,1):1}
    current_pos = (0,1)
    direction = right

    for i in range(3,limit):
        if direction == right:
            if (current_pos[0] + 1, current_pos[1]) not in grid.keys():
                current_pos = (current_pos[0] + 1, current_pos[1]) 
                direction = up
            else:
                current_pos =  (current_pos[0], current_pos[1]+1) 
        elif direction == left:
            if (current_pos[0] - 1, current_pos[1]) not in grid.keys():
                current_pos = (current_pos[0] - 1, current_pos[1]) 
                direction = down
            else:
                current_pos =  (current_pos[0], current_pos[1] - 1) 
        elif direction == up:
            if (current_pos[0], current_pos[1]-1) not in grid.keys():
                current_pos = (current_pos[0], current_pos[1]-1) 
                direction = left
            else:
                current_pos =  (current_pos[0]+1, current_pos[1]) 
        elif direction == down:
            if (current_pos[0], current_pos[1]+1) not in grid.keys():
                current_pos = (current_pos[0], current_pos[1]+1) 
                direction = right
            else:
                current_pos = (current_pos[0]-1, current_pos[1]) 
        
        grid[current_pos] = sum([grid.get((current_pos[0]-1, current_pos[1]-1),0),
                                 grid.get((current_pos[0]-1, current_pos[1]+1),0),
                                 grid.get((current_pos[0]-1, current_pos[1]  ),0),
                                 grid.get((current_pos[0]+1, current_pos[1]-1),0),
                                 grid.get((current_pos[0]+1, current_pos[1]+1),0),
                                 grid.get((current_pos[0]+1, current_pos[1]  ),0),
                                 grid.get((current_pos[0], current_pos[1]-1),0),
                                 grid.get((current_pos[0], current_pos[1]+1),0)])
        if grid[current_pos] > limit:
            print grid
            return current_pos, grid[current_pos]

def calc_steps(x):

    if x == 1:
        return 0

    index = 0
    val = 1
    while(True):
        right_bottom = val*val
        left_bottom = right_bottom - val + 1
        left_top = left_bottom - val + 1
        right_top = left_top - val + 1

        if x <= right_bottom:
            if x in [right_bottom, left_bottom, left_top, right_top]:
                return 2 * index
            elif right_bottom > x > left_bottom:
                return index + abs(index - (right_bottom - x))
            elif left_bottom > x > left_top:
                return index + abs(index - (left_bottom - x))
            elif left_top > x > right_top:
                return index + abs(index - (left_top - x))
            else: 
                return index + abs(index - (right_top - x))
        else:
            index += 1
            val += 2
            
            
if __name__ == '__main__':
   
    assert calc_steps(1) == 0 
    assert calc_steps(2) == 1 
    assert calc_steps(5) == 2 
    assert calc_steps(9) == 2 
    assert calc_steps(12) == 3
    assert calc_steps(23) == 2
    assert calc_steps(1024) == 31 
    
    print calc_steps(265149)
    print calc_grid(361)
    print calc_grid(265149)
