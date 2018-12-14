#!/usr/bin/env python

import sys, re

example_input1 = """/->-\        
|   |  /----\\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
\------/   """

example_input2 = """/>-<\  
|   |  
| /<+-\\
| | | v
\>+</ |
  |   ^
  \<->/"""

left = {
    (0, 1):(1,0),
    (1, 0):(0,-1),
    (0, -1):(-1,0),
    (-1, 0):(0,1)
}

right = {
    (0, 1):(-1,0),
    (-1, 0):(0,-1),
    (0, -1):(1,0),
    (1, 0):(0,1)
}

def part1(data, first=True):
    
    tracks = data.split("\n")
    cars = {}
    i = 0

    for y in range(0, len(tracks)):
        for x in range(0, len(tracks[y])):
            if tracks[y][x] == ">":
                cars[i] = [x, y, 1, 0, 0]
                i += 1
            if tracks[y][x] == "<":
                cars[i] = [x, y, -1, 0, 0]
                i += 1
            if tracks[y][x] == "^":
                cars[i] = [x, y, 0, -1, 0]
                i += 1
            if tracks[y][x] == "v":
                cars[i] = [x, y, 0, 1, 0]
                i += 1
        
        tracks[y] = tracks[y].replace(">", "-")
        tracks[y] = tracks[y].replace("<", "-")
        tracks[y] = tracks[y].replace("^", "|")
        tracks[y] = tracks[y].replace("v", "|")

    collision = False
    ticks = 0
    while len(cars) > 1:
        ticks += 1
        pos = set()
        j = 0
        for x in sorted(cars.values(), key=lambda x: (x[1],x[0])):
            j += 1
            cur_x, cur_y, vel_x, vel_y, nr_cross = x
            x[0] += x[2]
            x[1] += x[3]
            new_char = tracks[x[1]][x[0]]

            assert new_char in "/\\|-+"

            direc = None
            if new_char == "/":
                direc = right if x[2] == 0 else left
            if new_char == "\\":
                direc = left if x[2] == 0 else right 
            
            if new_char == "+":
                if x[4] == 0:  
                    direc = left 
                    x[4] = 1
                elif x[4] == 1:
                    x[4] = 2
                elif x[4] == 2:  
                    direc = right
                    x[4] = 0
            
            if direc is not None:
                x[2], x[3] = direc[(x[2], x[3])]

            new_coords = (x[0], x[1])
   
            if new_coords in [(s[0], s[1]) for s in cars.values() if s != x]:
                if first:
                    return new_coords

                for l, k in cars.items():
                    if k[0] == new_coords[0] and k[1] == new_coords[1]:
                        cars.pop(l)

            else:
                pos.add(new_coords)
    return (cars.values()[0][0], cars.values()[0][1]) 

if __name__ == '__main__':

    assert part1(example_input1) == (7,3)
    assert part1(example_input2, False) == (6,4)

    data = sys.argv[1]

    print part1(data)
    print part1(data, False)

