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


def count_regions(grid):


if __name__ == '__main__':

    grid = defrag("hwlqcszp")
    print count_used(grid)


