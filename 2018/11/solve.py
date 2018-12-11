#!/usr/bin/env python

import sys, re

def p_level(x,y,serial):
    rack = x + 10
    power = rack * y
    power += serial
    power *= rack
    power = int(str(power / 100)[-1]) if power > 100 else 0
    power -= 5

    return power

def part1(serial, sizes):

    grid = []
    for y in range(0, 299):
        row = []
        grid.append(row)
        for x in range(0,299):
            row.append(p_level(x+1, y+1, serial))

    most_val = 0
    most_coord = (0,0)

    for y in range(0,299):
        for x in range(0,299):
            s_val = 0
            max_s = max([-1] + [s for s in sizes if y+s < 299 and x+s < 299])

            for s in range(0, max_s):
                s_val += sum(grid[y+s][x:x+s+1])
                for i in range(0,s):
                    s_val += grid[y+i][x+s]

                if s_val > most_val:
                    most_val = s_val
                    most_coord = (x+1,y+1,s+1)

    return most_coord

if __name__ == '__main__':

    assert p_level(3,5,8) == 4
    assert p_level(122,79,57) == -5
    assert p_level(217,196,39) == 0

    assert part1(18,[1,2,3]) == (33,45,3)
    assert part1(42,[1,2,3]) == (21,61,3)
    
    print part1(8772, [1,2,3])
    print part1(8772, range(0,299))

