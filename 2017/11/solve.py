#!/usr/bin/env python

import sys
import math

moves = {"n":(0,1), "ne":(1,0), "se":(1,-1), "s":(0,-1), "sw":(-1,0), "nw":(-1,1)}

def calc_dist(steps):
    pos = [0,0]
    max_dist = 0

    for s in steps.split(","):
        pos[0] = pos[0] + moves[s][0]
        pos[1] = pos[1] + moves[s][1]
        
        # see: https://www.redblobgames.com/grids/hexagons/#distances
        dist = (abs(pos[0]) + abs(pos[0] + pos[1]) + abs(pos[1])) / 2
        if dist > max_dist:
            max_dist = dist

    return dist, max_dist

if __name__ == '__main__':
    
    assert calc_dist("ne,ne,ne") == (3,3)
    assert calc_dist("ne,ne,sw,sw") == (0,2)
    assert calc_dist("ne,ne,s,s") == (2,2)
    assert calc_dist("se,sw,se,sw,sw") == (3,3)

    print calc_dist(sys.argv[1])

