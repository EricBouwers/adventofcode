#!/usr/bin/env python

import sys, re

test_input = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""

def print_lights(lights):
    xs = [l[0] for l in lights.values()]
    ys = [l[1] for l in lights.values()]

    for y in range(min(ys), max(ys)+1): 
        line = []
        for x in range(min(xs), max(xs)+1):
            line.append("X" if [x,y] in lights.values() else ".")
        print "".join(line)

def part1(data):
    lights = [map(int, re.findall("-?\d+", line)) for line in data.split("\n")]
    coords = { i:[l[0], l[1]] for i,l in enumerate(lights)}
    velo   = { i:[l[2], l[3]] for i,l in enumerate(lights)}

    xs = [l[0] for l in coords.values()]
    ys = [l[1] for l in coords.values()]
    min_x, max_x = (min(xs), max(xs))
    min_y, max_y = (min(ys), max(ys))

    sky = (max_x - min_x) * (max_y - min_y) 
    old_sky = sky + 1
    seconds = 0
    
    while old_sky > sky:
        seconds += 1
        old_sky = sky
        min_x, max_x, min_y, max_y = (max_x, min_x, max_y, min_y)

        for i, c in coords.items():
            v = velo[i]
            c[0] += v[0]
            c[1] += v[1]
            coords[i] = c
            
            min_x = min(min_x, c[0])
            max_x = max(max_x, c[0])
            min_y = min(min_y, c[1])
            max_y = max(max_y, c[1])
   
        sky = (max_x - min_x) * (max_y - min_y) 
        
    for i, c in coords.items():
        v = velo[i]
        c[0] -= v[0]
        c[1] -= v[1]
        coords[i] = c

    print_lights(coords)   

    return seconds - 1

if __name__ == '__main__':

    assert part1(test_input) == 3

    data = sys.argv[1]

    print part1(data)

