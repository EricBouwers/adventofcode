#!/usr/bin/python

import sys
from itertools import permutations

df_out = sys.argv[1].split("\n")
w = 34
h = 30
grid = [[(None, None) for x in range(w)] for y in range(h)] 


min_used = 9999999999999999
max_avail= 0 
for l in df_out:
    parts = l.split()
    print parts
    if parts[0].startswith("/dev/grid"):
        x = int(parts[0].split("-")[1].replace("x",""))
        y = int(parts[0].split("-")[2].replace("y",""))

        used = int(parts[2].replace("T",""))
        avail = int(parts[3].replace("T",""))

        grid[y][x] = (used, avail)
        min_used = min(min_used, used)
        max_avail = max(max_avail, avail)

print min_used
print max_avail

found_pairs = 0
for x,y in [(x,y) for x in range(w) for y in range(h)]:
    for nx, ny in [(a,b) for a in range(w) for b in range(h)]:
        if (x,y) != (nx,ny):
            if grid[y][x][0] > 0 and grid[y][x][0] < grid[ny][nx][1]:
                print x,y,nx,ny
                found_pairs += 1

print found_pairs

for r in grid:
    print " ".join(["_" if c[0] == 0 else "#" if c[0] >= max_avail else "." for c in r])

print "just count the right dots, 5 per moving G one step closer"    
