#!/usr/bin/env python

import sys, re

def part1(depth, tx, ty):

    icave = []
    tcave = []
    risk = 0
    for y in range(0, ty+5):
        irow = []
        icave.append(irow)
        trow = []
        tcave.append(trow)
        for x in range(0, tx+5):
            
            if (x,y) in [(0,0), (tx, ty)]:
                irow.append((0 + depth) % 20183)
            elif y == 0:
                irow.append((x*16807 + depth) % 20183)
            elif x == 0:
                irow.append((y*48271 + depth) % 20183)
            else:
                irow.append((irow[-1] * icave[-2][x] + depth) % 20183)
            
            if (x,y) in [(0,0), (tx, ty)]:
                trow.append("M" if x == 0 else "T")
            else:
                t_mod = irow[-1] % 3    
                risk += t_mod if x <= tx and y <= ty else 0
                trow.append("." if t_mod == 0 else "=" if t_mod == 1 else "|")    

    return risk, tcave

def part2(depth, tx, ty):

    _, tcave = part1(depth, tx, ty)
    return None

if __name__ == '__main__':

    assert part1(510, 10, 10)[0] == 114
    assert part2(510, 10, 10) == 45

    print part1(8103, 9, 758)[0]

