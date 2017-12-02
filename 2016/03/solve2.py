#!/usr/bin/python

import sys, operator

lines = sys.argv[1].split("\n")
valid = 0

for i in xrange(0,len(lines),3):
    
    line1 = lines[i].split()
    line2 = lines[i+1].split()
    line3 = lines[i+2].split()

    parts = []

    for i in xrange(0, 3):
        parts.append([line1[i], line2[i], line3[i]])

    print parts
    
    for part in parts:
        x1 = int(part[0])
        x2 = int(part[1])
        x3 = int(part[2])

        if all([x1 + x2 > x3, x1 + x3 > x2, x2 + x3 > x1]): 
            valid += 1

print valid
