#!/usr/bin/python

import sys, operator

lines = sys.argv[1].split("\\n")
row = 1
column = 1

for line in lines:
    for char in line:
        if char == "U":
            row = row - 1 if row > 0 else 0
  
        if char == "D":
            row = row + 1 if row < 2 else 2
        
        if char == "L":
            column = column - 1 if column > 0 else 0
  
        if char == "R":
            column = column + 1 if column  < 2 else 2
    
    print row * 3 + column + 1



