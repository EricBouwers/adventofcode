#!/usr/bin/env python

import sys
from collections import deque

example = """..#\n#..\n..."""


def parse(start, bursts):
    bursts = bursts / 2
    parts = start.split("\n")
    grid = []

    for i in range(0, bursts):
        row = [0] * (2 * bursts + len(parts))
        grid.append(row)
    
    for i in range(0, len(parts)):
        row = [0] * bursts
        row += map(lambda x: 1 if x == "#" else 0, parts[i])
        row += [0] * bursts
        grid.append(row)
    
    for i in range(0, bursts):
        row = [0] * (2 * bursts + len(parts))
        grid.append(row)

    return grid


def execute(start, bursts):
    infected = 0
    grid = parse(start, bursts)
    cur_pos = [len(grid) / 2, len(grid) / 2]
    dirs = deque([[0,-1], [1,0], [0,1], [-1,0]])

    for i in range(0, bursts):
        if grid[cur_pos[1]][cur_pos[0]]:
            dirs.rotate(-1)
        else:    
            infected += 1
            dirs.rotate(1)

        grid[cur_pos[1]][cur_pos[0]] = not grid[cur_pos[1]][cur_pos[0]] 
        cur_pos[0] += dirs[0][0]
        cur_pos[1] += dirs[0][1]

    return infected 


def execute_2(start, bursts, size):
    infected = 0
    grid = parse(start, size)
    
    cur_pos = [len(grid) / 2, len(grid) / 2]
    dirs = deque([[0,-1], [1,0], [0,1], [-1,0]])
    changes = {0:2, 2:1, 1:3, 3:0}

    for i in range(0, bursts):
        # 0 = clean, 1 = infected, 2 = weakened, 3 = flagged
        if grid[cur_pos[1]][cur_pos[0]] == 1:
            dirs.rotate(-1)
        elif grid[cur_pos[1]][cur_pos[0]] == 0:    
            dirs.rotate(1)
        elif grid[cur_pos[1]][cur_pos[0]] == 3:
            dirs.rotate(2)
        else:
            infected += 1

        grid[cur_pos[1]][cur_pos[0]] = changes[grid[cur_pos[1]][cur_pos[0]] ]

        cur_pos[0] += dirs[0][0]
        cur_pos[1] += dirs[0][1]

    return infected 


if __name__ == '__main__':
    
    assert execute(example, 7) == 5
    assert execute(example, 70) == 41
    assert execute(example, 10000) == 5587
    
    print execute(sys.argv[1], 10000)
    
    assert execute_2(example, 100, 50) == 26
    assert execute_2(example, 10000000, 1000) == 2511944
    
    print execute_2(sys.argv[1], 10000000, 1000)




