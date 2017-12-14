#!/usr/bin/env python

import sys
from collections import deque

def execute(x, lengths, skip, index):
    x_len = len(x)

    for l in lengths:
        end_index = index+l

        if end_index > x_len:
            extra = end_index % x_len
            d = deque(x)
            d.rotate(0-extra)
            x = list(d)
            x = [-1]*extra + x

        interested_in = x[index:end_index]
        new_values = list(reversed(interested_in))
        x = x[0:index] + new_values + x[end_index:] 
        
        if end_index > x_len:
            x = x[extra:]
            d = deque(x)
            d.rotate(extra)
            x = list(d)

        index = (index + l + skip) % x_len
        skip += 1

    return x[0]*x[1], skip, index, x

def knot_hash(x, lengths):
    lengths = map(ord,lengths)
    lengths += [17, 31, 73, 47, 23]

    index = 0
    skip = 0
    for i in range(0,64):
        h, skip, index, x = execute(x, lengths, skip, index)

    result = []
    for i in range(0,256,16):
        result.append(reduce(lambda x, y: x^y, x[i:i+16]) )

    return reduce(lambda i,j: i+ "%0.2x" % j, result, "")


def defrag(key):
    grid = []        

    for i in range(0, 128):
        row_hash = knot_hash(range(0,256), "{}-{}".format(key, i))
        
        line = ""    
        for c in row_hash:
            line += format(int(c, 16), 'b').zfill(4)
            
        grid.append([int(x) for x in line])
    
    return grid 


def count_used(grid):
    return sum([sum(x) for x in grid])


def pos_key(i,j):
    return "{}_{}".format(i,j)


def count_regions(grid):
    seen = set()
    groups = 0

    for i in range(0, 128):
        for j in range(0, 128):
            if grid[i][j] == 1 and pos_key(i,j) not in seen:
                add_nodes(grid, i, j, seen)
                groups += 1
    
    return groups


def add_nodes(grid, i, j, all_nodes):
    if pos_key(i,j) not in all_nodes:
        all_nodes.add(pos_key(i,j))

        for newi, newj in attached(grid, i, j):
            add_nodes(grid, newi, newj, all_nodes)


def attached(grid, i, j):
    return filter(None, [(i+1, j) if i < 127 and grid[i+1][j] == 1 else None 
                        ,(i-1, j) if i > 0 and grid[i-1][j] == 1 else None      
                        ,(i, j+1) if j < 127 and grid[i][j+1] == 1 else None           
                        ,(i, j-1) if j > 0 and grid[i][j-1] == 1 else None])


if __name__ == '__main__':

    grid = defrag("hwlqcszp")
    print count_used(grid)
    print count_regions(grid)


