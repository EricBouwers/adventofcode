#!/usr/bin/python

import sys

instructions= sys.argv[1].split("\n")

w, h = 50, 6
display = [["." for x in range(w)] for y in range(h)] 

def printdisplay():
    for row in display:
        print "".join(row)

def countdisplay():
    c = 0
    for row in display:
        for col in row:
             c += 1 if col == "#" else 0
    print c         

for inst in instructions:
    if "rect" in inst:
        size = inst.split()[1].split("x")
        for i in range(0,int(size[0])):
            for j in range(0, int(size[1])):
                display[j][i] = "#"
    if "column" in inst:
        col = int(inst.split()[2].split("=")[1])
        steps = int(inst.split()[4])
        old_val = None
        for s in range(0, steps):
            for i in range(0,h):
                prev_val = display[i][col]
                display[i][col] = old_val
                old_val = prev_val
            display[0][col] = old_val
    if "row" in inst:
        row = display[int(inst.split()[2].split("=")[1])]
        steps = int(inst.split()[4])
        
        for i in range(0,steps):
            row.insert(0,row.pop())


    printdisplay()
    print "///////////"

printdisplay()
countdisplay()
