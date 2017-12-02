#!/usr/bin/python

import sys, operator

lines = sys.argv[1].split("\n")
valid = 0

for line in lines:
    parts = line.split()

    x1 = int(parts[0])
    x2 = int(parts[1])
    x3 = int(parts[2])

    if all([x1 + x2 > x3, x1 + x3 > x2, x2 + x3 > x1]): 
        valid += 1

print valid
