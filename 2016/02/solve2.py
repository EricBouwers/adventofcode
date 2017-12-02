#!/usr/bin/python

import sys, operator

lines = sys.argv[1].split("\\n")
row = 2
column = 0

keypad = [
 [None, None, 1  , None, None]
,[None, 2   , 3  , 4   , None]
,[5   , 6   , 7  , 8   , 9   ]
,[None, "A" , "B", "C" , None]
,[None, None, "D", None, None]
]

for line in lines:
    for char in line:
        if char == "U":
            row = row - 1 if row > 0 and keypad[row-1][column] is not None else row
  
        if char == "D":
            row = row + 1 if row < len(keypad) -1 and  keypad[row+1][column] is not None else row 
        
        if char == "L":
            column = column - 1 if column > 0 and keypad[row][column-1] is not None else column 
  
        if char == "R":
            column = column + 1 if column < len(keypad[0])-1 and keypad[row][column+1] is not None else column 
    
    print keypad[row][column] 



