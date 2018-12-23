#!/usr/bin/env python

import sys, re, operator, collections

example_input_1 = """pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1"""

example_input_2 = """pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5"""

def man_dist(x,y):
    return sum([abs(x[i] - y[i]) for i in range(0, 3)])

def get_bots(data):
    bots = [map(int, re.findall("-?\d+", line)) for line in data.split("\n")]
    bots.sort(key=lambda x: x[-1])
    return bots

def part1(data):
    bots = get_bots(data)
    
    strongest = bots[-1]
    srange = strongest[-1]

    return sum([1 if man_dist(b, strongest) <= srange else 0 for b in bots])

def part2(data):
    bots = get_bots(data)

    xs = [x[0] for x in bots]
    ys = [x[1] for x in bots]
    zs = [x[2] for x in bots]

    drange = 1
    while drange < max(xs) - min(xs):
        drange *= 2

    while True:
        highest = 0
        closest = None
        
        for x in xrange(min(xs), max(xs) + 1, drange):
            for y in xrange(min(ys), max(ys) + 1, drange):
                for z in xrange(min(zs), max(zs) + 1, drange):
                    inrange = sum([1 if (man_dist(b, (x,y,z)) - b[3]) / drange <= 0 else 0 for b in bots])
                    if inrange > highest or (inrange == highest and man_dist((x,y,z), (0,0,0)) < closest):
                        highest = inrange
                        closest = [x,y,z]

        if drange == 1:
            return man_dist(closest, (0,0,0)) 
        else:
            xs = [closest[0] - drange, closest[0] + drange]
            ys = [closest[1] - drange, closest[1] + drange]
            zs = [closest[2] - drange, closest[2] + drange]
            drange /= 2

if __name__ == '__main__':

    assert part1(example_input_1) == 7
    assert part2(example_input_2) == 36

    data = sys.argv[1]

    print part1(data)
    print part2(data)

