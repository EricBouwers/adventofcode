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

if __name__ == '__main__':
    
    assert execute(range(0,5),[3,4,1,5], 0, 0) == (12, 4, 4, [3,4,2,1,0])
    assert knot_hash(range(0,256), "") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert knot_hash(range(0,256), "AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert knot_hash(range(0,256), "1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert knot_hash(range(0,256), "1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

    print execute(range(0,256), [46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204], 0, 0)
    print knot_hash(range(0,256), "46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204")



